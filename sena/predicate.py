import typing as t

from .handler import HandlerFn, Endpoint
from .control_flow import ControlFlow, Continue

C = t.TypeVar("C")
B = t.TypeVar("B")

C_contra = t.TypeVar("C_contra", contravariant=True)

class PredicateFn(t.Protocol[C_contra]):
    def __call__(self, req: C_contra, /) -> bool:
        ...

class Predicate(HandlerFn[B, C]):
    __slots__ = ('pred', 'handler')

    def __init__(self, pred: PredicateFn[C], handler: HandlerFn[B, C]) -> None:
        self.pred = pred
        self.handler = handler

    async def __call__(self, req: C, next: Endpoint[B, C], /) -> ControlFlow[B, C]:
        if self.pred(req):
            return await self.handler(req, next)
        return Continue(req)


__all__ = ["PredicateFn", "Predicate"]

