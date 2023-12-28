from __future__ import annotations
from dataclasses import dataclass
from types import EllipsisType
from typing import (
    ParamSpec,
    Concatenate,
    Callable,
    TypeVar,
    TypeAlias,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from .session import Session
    from .gate import MethodCall

from ..utils.typing import MaybeException
from ..middlewares import Middleware
from ..middlewares.extended import Group
from ..utils.hof import Alter1Marker, alter1_ellipsis

T0 = TypeVar("T0")
T1 = TypeVar("T1")
R = TypeVar("R")
P = ParamSpec("P")


def apply_last(f: Callable[[T0, T1], R], v: T1) -> Callable[[T0], R]:
    return lambda first: f(first, v)


def replace_or_and(
    lhs: SessionMiddleware[P] | None,
    rhs: SessionMiddleware[P] | None,
) -> SessionMiddleware[P] | None:
    if lhs is None and rhs is None:
        return None
    elif lhs is None:
        return rhs
    elif rhs is None:
        return lhs
    return Group(lhs, rhs)


@dataclass(slots=True, frozen=True)
class SessionMiddlewares:
    before: SessionMiddleware[[]] | None = None
    after: SessionMiddleware[[MaybeException]] | None = None

    def __and__(self, rhs: SessionMiddlewares) -> SessionMiddlewares:
        return self.alter(
            before=apply_last(replace_or_and, rhs.before),
            after=apply_last(replace_or_and, rhs.after),
        )

    def alter(
        self,
        *,
        before: Alter1Marker[SessionMiddleware[[]] | None, EllipsisType] | None = None,
        after: Alter1Marker[SessionMiddleware[[MaybeException]] | None, EllipsisType]
        | None = None,
    ) -> SessionMiddlewares:
        return SessionMiddlewares(
            before=alter1_ellipsis(before, self.before),
            after=alter1_ellipsis(after, self.after),
        )


SessionMiddleware: TypeAlias = Middleware[Concatenate["Session", "MethodCall", P], None]

__all__ = [
    "SessionMiddleware",
    "SessionMiddlewares",
]
