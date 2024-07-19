import typing as t


from ..handling.handler import HandlerFn
from ..handling.reduction import Reducing

from ..types.handler_meta_info import HandlerMetaInfo


@t.runtime_checkable
class CollectMetaInfo(t.Protocol):
    def collect_meta_info(self) -> HandlerMetaInfo:
        ...

def collect_meta_info(initial: HandlerMetaInfo, handler: HandlerFn[t.Any]) -> HandlerMetaInfo:
    if isinstance(handler, CollectMetaInfo):
        return initial.combine(handler.collect_meta_info())
    elif isinstance(handler, Reducing):
        return handler.reduce(collect_meta_info, initial)

    return initial


__all__ = ["CollectMetaInfo"]

