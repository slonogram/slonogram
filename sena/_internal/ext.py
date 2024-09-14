from __future__ import annotations

import typing as t

from .apply import Apply
from .then import Then
from .continued import Continued, AsyncContinued

from .base import (
    Handler,
    AsyncHandler,
    SeqHandler,
)

from .modify import Modify
from .reducible import Reducible, Reducer

In = t.TypeVar("In")
On = t.TypeVar("On")

I = t.TypeVar("I")
N = t.TypeVar("N")

P = t.ParamSpec("P")
O = t.TypeVar("O")

M = t.TypeVar("M", bound=Modify)
Res = t.TypeVar("Res")

Re = t.TypeVar("Re", bound=Reducible)
Acc = t.TypeVar("Acc")

Inner = t.TypeVar("Inner")

Opaque = t.TypeVar("Opaque")

# This is required cause python kinda suck.
class Ext(t.Generic[Inner]):
    __slots__ = ('inner', )

    def __init__(self, inner: Inner) -> None:
        self.inner = inner

    def __repr__(self) -> str:
        return repr(self.inner)

    def __call__(
        self: Ext[t.Callable[P, O]],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> O:
        return self.inner(*args, **kwargs)

    def untyped_modify(self, f: t.Callable[[t.Any], t.Any]) -> t.Any:
        """Type hints don't have HKTs, so `modify` is not powerful enough.
        """
        if isinstance(self.inner, Modify):
            return type(self)(self.inner.modify(f))
        return type(self)(f(self.inner))

    def reduce(self: Ext[Re], f: Reducer[Acc], initial: Acc) -> Acc:
        return self.inner.reduce(f, initial)

    # Sugar

    # Basically same as `.apply`, but inverted.
    def after(
        self: Ext[N],
        seq: SeqHandler[I, O, N],
    ) -> Ext[Handler[I, O]]:
        return self.untyped_modify(lambda inner: Apply(seq, inner))

    def apply(
        self: Ext[SeqHandler[I, O, N]],
        next: N,
    ) -> Ext[Handler[I, O]]:
        return self.untyped_modify(lambda lhs: Apply(lhs, next))

    # Some type erasure performed, hope it helps.
    def then(
        self: Ext[Handler[I, O]],
        next: N,
    ) -> Ext[Then[Handler[I, O], N]]:
        return self.untyped_modify(lambda lhs: Then(lhs, next))

    def continued(
        self: Ext[Handler[I, O]],
    ) -> Ext[Continued[Handler[I, O]]]:
        return self.untyped_modify(Continued)

    def acontinued(
        self: Ext[AsyncHandler[I, O]],
    ) -> Ext[AsyncContinued[AsyncHandler[I, O]]]:
        return self.untyped_modify(AsyncContinued)
