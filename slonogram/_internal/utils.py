from types import EllipsisType
from io import IOBase
from typing import TypeVar, TypeAlias, Callable, Any

from ..session import CanCollectAttachs

T = TypeVar("T")

AlterFn: TypeAlias = Callable[[T], T | EllipsisType]


def prefer(val: Any | EllipsisType, otherwise: Any) -> Any:
    if val is ...:
        return otherwise
    return val


def collect_attachs_from(
    obj: CanCollectAttachs | list,
    dest: dict[str, IOBase],
) -> None:
    if isinstance(obj, list):
        for item in obj:
            collect_attachs_from(item, dest)
    else:
        obj.collect_attachs(dest)
