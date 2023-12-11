from __future__ import annotations
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from typing import (
    TypeVar,
    Generic,
    TypeAlias,
    Iterable as Y,
    Callable,
    overload,
    cast,
    Any,
    Type,
)

from .handler import RawHandler, Handler

from ..schemas import Message, CallbackQuery, InlineQuery
from ..utils import origin_of
from ..filtering.base import BareFilter

from ..types import interest as I
from ..types.interest import Interest


C = TypeVar("C", contravariant=True)
M = TypeVar("M", covariant=True)
T = TypeVar("T")
R = TypeVar("R")

MessageCompat: TypeAlias = I.MessageI | I.EditedMessageI
CallbackQCompat: TypeAlias = I.CallbackQueryI
InlineQCompat: TypeAlias = I.InlineQueryI

RelaxedCompat: TypeAlias = Interest


class Filter(Generic[M]):
    __slots__ = ()


@dataclass(slots=True, frozen=True)
class _Disamb(Generic[T]):
    tp: Type[T]
    val: T


def disamb(tp: Type[T], val: T) -> _Disamb[T]:
    return _Disamb(tp, val)


def identity(x: T) -> T:
    return x


class Interested(Generic[C, T]):
    __slots__ = ("interests", "handler")

    def __init__(self, interests: set[Interest], handler: T) -> None:
        self.interests = interests
        self.handler = handler

    def bimap(
        self, f: Callable[[set[Interest], T], tuple[set[Interest], R]]
    ) -> Interested[C, R]:
        interests, handler = f(self.interests, self.handler)
        return Interested[C, R](interests, handler)

    def map(self, f: Callable[[T], R]) -> Interested[C, R]:
        return self.bimap(lambda s, h: (s, f(h)))

    def _yield(self, interest: Interest) -> Y[T]:
        if interest in self.interests:
            yield self.handler
        yield from ()

    def message(self) -> Y[T]:
        return self._yield(Interest.MESSAGE)

    def edited_message(self) -> Y[T]:
        return self._yield(Interest.EDITED_MESSAGE)

    def callback_query(self) -> Y[T]:
        return self._yield(Interest.CALLBACK_QUERY)

    def inline_query(self) -> Y[T]:
        return self._yield(Interest.INLINE_QUERY)


class _Combinator(Generic[T, C, M], metaclass=ABCMeta):
    interests: set[Interest]

    @abstractmethod
    def _combine(self, rhs: _Combinator[T, C, M]) -> T:
        raise NotImplementedError

    def __or__(self, rhs: _Combinator[T, C, M]) -> T:
        return self._combine(rhs)


class InterestCombinator(_Combinator["InterestCombinator[C, M]", C, M]):
    __slots__ = ("interests",)

    def __init__(self, interests: set[Interest]) -> None:
        self.interests = interests

    def _combine(
        self, rhs: _Combinator[InterestCombinator[C, M], C, M]
    ) -> InterestCombinator[C, M]:
        return InterestCombinator[C, M]({*self.interests, *rhs.interests})

    @overload
    def __gt__(self, rhs: RawHandler[M]) -> Interested[C, RawHandler[M]]:
        ...

    @overload
    def __gt__(self, rhs: Handler[M]) -> Interested[C, Handler[M]]:
        ...

    @overload
    def __gt__(self, rhs: _Disamb[Handler[M]]) -> Interested[C, Handler[M]]:
        ...

    @overload
    def __gt__(self, rhs: _Disamb[Filter[M]]) -> Interested[C, BareFilter[M]]:
        ...

    def __gt__(
        self,
        rhs: Any,
    ) -> Any:
        if isinstance(rhs, _Disamb):
            origin = origin_of(rhs.tp)
            if origin is Handler:
                return Interested[C, Handler[M]](self.interests, rhs.val)
            elif origin is Filter:
                return Interested[C, BareFilter[M]](self.interests, rhs.val)
        elif isinstance(rhs, Handler):
            return Interested[C, Handler[M]](self.interests, rhs)

        # RawHandler here
        return Interested[C, RawHandler[M]](self.interests, rhs)


def relax(comb: InterestCombinator[C, M]) -> InterestCombinator[RelaxedCompat, Any]:
    """Relaxes typing requirements for the combinator"""
    return cast(InterestCombinator[RelaxedCompat, Any], comb)


MessageComb: TypeAlias = InterestCombinator[MessageCompat, Message]
CallbackQComb: TypeAlias = InterestCombinator[CallbackQCompat, CallbackQuery]
InlineQComb: TypeAlias = InterestCombinator[InlineQCompat, InlineQuery]

message = MessageComb({Interest.MESSAGE})
edited_message = MessageComb({Interest.EDITED_MESSAGE})
callback_query = CallbackQComb({Interest.CALLBACK_QUERY})
inline_query = InlineQComb({Interest.INLINE_QUERY})

# fmt: off

message_r        = relax(message)
edited_message_r = relax(edited_message)
callback_query_r = relax(callback_query)
inline_query_r   = relax(inline_query)

# fmt: on

__all__ = [
    "InterestCombinator",
    "Interested",
    #
    # Combinators
    #
    "message",
    "edited_message",
    "callback_query",
    "inline_query",
    #
    # Relaxed version
    #
    "message_r",
    "edited_message_r",
    "callback_query_r",
    "inline_query_r",
]
