from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from .then import Then
    from .apply import Apply

from .base import Handler, Predicate, SeqHandler
from .modify import Modify
from .reducible import Reducible

Acc = t.TypeVar("Acc")

Inner = t.TypeVar("Inner")
Output = t.TypeVar("Output")

I = t.TypeVar("I", contravariant=True)
O = t.TypeVar("O", covariant=True)
N = t.TypeVar("N", contravariant=True)

Next = t.TypeVar("Next")
Cur = t.TypeVar("Cur")


class HandlerExt(Modify, Reducible, t.Protocol):
    def after(
        self,
        current: SeqHandler[I, O, t.Self],
    ) -> ExtendedHandler[I, O]:
        from .apply import Apply

        return Apply[SeqHandler[I, O, t.Self], t.Self](current, self)


class PredicateExt(HandlerExt, t.Protocol):
    def __and__(self: Predicate[I], rhs: Predicate[I]) -> ExtendedPredicate[I]:
        from .binary import Binary, and_

        return Binary[Predicate[I], Predicate[I], t.Any](self, rhs, and_)

    def __or__(self: Predicate[I], rhs: Predicate[I]) -> ExtendedPredicate[I]:
        from .binary import Binary, or_

        return Binary[Predicate[I], Predicate[I], t.Any](self, rhs, or_)

    def __xor__(self: Predicate[I], rhs: Predicate[I]) -> ExtendedPredicate[I]:
        from .binary import Binary, xor

        return Binary[Predicate[I], Predicate[I], t.Any](self, rhs, xor)

    def __invert__(self: Predicate[I]) -> ExtendedPredicate[I]:
        from .unary import Unary, not_

        return Unary[Predicate[I], t.Any](self, not_)

    def not_(self: Predicate[I]) -> ExtendedPredicate[I]:
        from .unary import Unary, not_

        return Unary[Predicate[I], t.Any](self, not_)


# Handler[I, O] & HandlerExt
class ExtendedHandler(HandlerExt, Handler[I, O], t.Protocol[I, O]): ...


# Predicate[I] & PredicateExt
class ExtendedPredicate(ExtendedHandler[I, bool], t.Protocol[I]): ...


class SeqHandlerExt(Modify, Reducible, t.Protocol):
    def apply(
        self: SeqHandler[I, O, N],
        next: N,
    ) -> ExtendedHandler[I, O]:
        from .apply import Apply

        return Apply[SeqHandler[I, O, N], N](self, next)

    def then(
        self: SeqHandler[I, O, "Apply[Next, N]"],
        next: N,
    ) -> "Then[SeqHandler[I, O, Apply[Next, N]], N]":
        from .then import Then

        return Then(self, next)


# SeqHandler[I, O, N] & SeqHandlerExt
class ExtendedSeqHandler(SeqHandlerExt, SeqHandler[I, O, N], t.Protocol[I, O, N]): ...
