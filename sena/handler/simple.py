import typing as t

from .base import HandlerFn, Next
from .extended import Handler, Mapper

from ..control_flow import ControlFlow
from ..utils import extract_handler

B = t.TypeVar("B")
C = t.TypeVar("C")


class Simple(Handler[B, C]):
    __slots__ = ('inner', )

    def __init__(self, inner: HandlerFn[B, C]) -> None:
        self.inner = extract_handler(inner)

    def map(self, f: Mapper[B, C]) -> t.Self:
        return type(self)(f(self.inner))

    def __call__(self, req: C, next: Next[B, C]) -> t.Awaitable[ControlFlow[B, C]]:
        return self.inner(req, next)


__all__ = ["Simple"]


