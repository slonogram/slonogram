from __future__ import annotations
from typing import (
    TypeVar,
    Generic,
    TypeAlias,
    Literal,
    Iterable as Y,
    Callable,
    overload,
    cast,
    Any,
)

from .handler import RawHandler, Handler

from ..schemas import Message, CallbackQuery, InlineQuery
from ..types.interest import Interest


C = TypeVar("C", contravariant=True)
M = TypeVar("M", covariant=True)
T = TypeVar("T")
R = TypeVar("R")

MessageCompat: TypeAlias = Literal[Interest.MESSAGE] | Literal[Interest.EDITED_MESSAGE]
CallbackQCompat: TypeAlias = Literal[Interest.CALLBACK_QUERY]
InlineQCompat: TypeAlias = Literal[Interest.INLINE_QUERY]

RelaxedCompat: TypeAlias = Interest


def identity(x: T) -> T:
    return x


class InterestedHandler(Generic[T]):
    __slots__ = ("interests", "handler")

    def __init__(self, interests: set[Interest], handler: T) -> None:
        self.interests = interests
        self.handler = handler

    def bimap(
        self, f: Callable[[set[Interest], T], tuple[set[Interest], R]]
    ) -> InterestedHandler[R]:
        interests, handler = f(self.interests, self.handler)
        return InterestedHandler[R](interests, handler)

    def map(self, f: Callable[[T], R]) -> InterestedHandler[R]:
        return self.bimap(lambda s, h: (s, f(h)))

    def _yield(self, interest: Interest) -> Y[T]:
        if interest in self.interests:
            yield self.handler
        yield from ()

    def message(self) -> Y[T]:
        return self._yield(Interest.MESSAGE)

    def edited_message(self) -> Y[T]:
        return self._yield(Interest.EDITED_MESSAGE)


class InterestCombinator(Generic[C, M]):
    __slots__ = ("interests",)

    def __init__(self, interests: set[Interest]) -> None:
        self.interests = interests

    def __or__(self, rhs: InterestCombinator[C, M]) -> InterestCombinator[C, M]:
        return InterestCombinator[C, M]({*self.interests, *rhs.interests})

    @overload
    def __gt__(self, rhs: RawHandler[M]) -> InterestedHandler[RawHandler[M]]:
        ...

    @overload
    def __gt__(self, rhs: Handler[M]) -> InterestedHandler[Handler[M]]:
        ...

    def __gt__(
        self,
        rhs: RawHandler[M] | Handler[M],
    ) -> InterestedHandler[Handler[M]] | InterestedHandler[RawHandler[M]]:
        # This is just for mypy to stfu
        if isinstance(rhs, Handler):
            return InterestedHandler[Handler[M]](self.interests, rhs)
        return InterestedHandler[RawHandler[M]](self.interests, rhs)


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
    "InterestedHandler",
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
