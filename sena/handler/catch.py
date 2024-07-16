import typing as t
import dataclasses as dtc

from .base import HandlerFn, HandlerFnFactory, Next
from ..control_flow import ControlFlow, Continue, Break

C = t.TypeVar("C")
B = t.TypeVar("B")
E = t.TypeVar("E")

@dtc.dataclass(slots=True)
class CaughtException(t.Generic[B, C]):
    exception: Exception
    request: C
    handler: HandlerFn[B, C]
    next: Next[B, C]


class ExceptionHandler(t.Protocol[B, C], Next[B, CaughtException[B, C]]):
    ...


class Catch(HandlerFn[B, C]):
    __slots__ = ('handler', 'exc_handler')

    def __init__(self, exc_handler: ExceptionHandler[B, C], handler: HandlerFn[B, C]) -> None:
        self.handler = handler
        self.exc_handler = exc_handler

    @classmethod
    def factory(cls, exc_handler: ExceptionHandler[B, C]) -> HandlerFnFactory[B, C, B, C]:
        return lambda handler: cls(exc_handler, handler)

    def __repr__(self) -> str:
        return f"Catch(handler={self.handler!r})"

    async def __call__(self, req: C, next: Next[B, C]) -> ControlFlow[B, C]:
        try:
            return await self.handler(req, next)
        except Exception as exc:
            result = await self.exc_handler(CaughtException(
                exception=exc,
                request=req,
                handler=self.handler,
                next=next,
            ))
            if isinstance(result, Continue):
                return Continue(result.value.request)
            return Break(result.value)


__all__ = ["Catch"]


