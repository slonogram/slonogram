import typing as t

from .base import HandlerFn, Next, HandlerFnFactory
from ..control_flow import ControlFlow, Continue
from ..utils import extract_handler

C = t.TypeVar("C")
B = t.TypeVar("B")

C_contra = t.TypeVar("C_contra", contravariant=True)

class Predicate(t.Protocol[C_contra]):
    def __call__(self, req: C_contra, /) -> bool:
        ...

class Filtered(HandlerFn[B, C]):
    __slots__ = ('pred', 'handler')

    def __init__(self, pred: Predicate[C], handler: HandlerFn[B, C]) -> None:
        self.pred = pred
        self.handler = extract_handler(handler)

    @classmethod
    def factory(cls, pred: Predicate[C]) -> HandlerFnFactory[B, C, B, C]:
        return lambda handler: cls(pred, handler)

    async def __call__(self, req: C, next: Next[B, C], /) -> ControlFlow[B, C]:
        if self.pred(req):
            return await self.handler(req, next)
        return Continue(req)


__all__ = ["Predicate", "Filtered"]

