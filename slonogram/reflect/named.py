from typing import Protocol, Any, overload, TypeVar
from ..omittable import OMIT, Omit

T = TypeVar("T")

class Named(Protocol):
    __name__: str

@overload
def get_name(val: Any) -> str | None: ...

@overload
def get_name(val: Any, default: T) -> str | T: ...

def get_name(val: Any, default: Any = OMIT):
    if isinstance(default, Omit):
        return getattr(val, '__name__', None)
    return getattr(val, '__name__', default)


__all__ = ["Named", "get_name"]

