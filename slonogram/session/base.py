from typing import Protocol, Awaitable, Any
from ..types.request import Request

class Session(Protocol):
    def __call__(self, req: Request, /) -> Awaitable[Any]:
        ...


__all__ = ["Session"]

