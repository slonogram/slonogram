from typing import Protocol, Awaitable, Any, Iterable, Self, overload
from functools import reduce

from .base import Session
from .extended import ExtendedSession

from ..types.request import Request


class SessionMiddleware(Protocol):
    def __call__(self, req: Request, next: Session, /) -> Awaitable[Any]:
        ...


class Follows(ExtendedSession):
    __slots__ = ('current', 'next')

    def __init__(self, next: Session, current: SessionMiddleware) -> None:
        self.current = current
        self.next = next

    @overload
    @classmethod
    def from_iterable(cls, session: ExtendedSession, middlewares: Iterable[SessionMiddleware]) -> ExtendedSession:
        ...

    @overload
    @classmethod
    def from_iterable(cls, session: Session, middlewares: Iterable[SessionMiddleware]) -> Session:
        ...

    @classmethod
    def from_iterable(cls, session: Session, middlewares: Iterable[SessionMiddleware]) -> Session:
        return reduce(cls, middlewares, session)

    def __call__(self, req: Request) -> Awaitable[Any]:
        return self.current(req, self.next)


__all__ = ["SessionMiddleware"]


