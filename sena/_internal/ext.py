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

    def modify(self: Ext[M], f: t.Callable[[M], Res], /) -> Ext[Res]:
        return Ext(self.inner.modify(f))

    def reduce(self: Ext[Re], f: Reducer[Acc], initial: Acc) -> Acc:
        return self.inner.reduce(f, initial)

    # Sugar

    # Basically same as `.apply`, but inverted.
    def after(
        self: Ext[N],
        seq: SeqHandler[I, O, N],
    ) -> Ext[Handler[I, O]]:
        return Ext(Apply(seq, self.inner))


    def apply(
        self: Ext[SeqHandler[I, O, N]],
        next: N,
    ) -> Ext[Handler[I, O]]:
        return Ext(Apply(self.inner, next))


    # Forgive me Lord for not erasing
    # return type of these functions.
    def then(
        self,
        next: N,
    ) -> Ext[Then[Inner, N]]:
        return Ext(Then(self.inner, next))

    def continued(
        self: Ext[Handler[I, O]],
    ) -> Ext[Continued[Handler[I, O]]]:
        return Ext(Continued(self.inner))

    def acontinued(
        self: Ext[AsyncHandler[I, O]],
    ) -> Ext[AsyncContinued[AsyncHandler[I, O]]]:
        return Ext(AsyncContinued(self.inner))
