from __future__ import annotations
from typing import (
    TypeVar,
    Generic,
    TypeAlias,
    Literal,
    Iterable as Y,
    Callable,
    overload,
)

from .handler import RawHandler, Handler

from ..schemas import Message, CallbackQuery
from ..types.interest import Interest


C = TypeVar("C", contravariant=True)
M = TypeVar("M")
T = TypeVar("T")
R = TypeVar("R")

MessageCompat: TypeAlias = Literal[Interest.MESSAGE] | Literal[Interest.EDITED_MESSAGE]
CallbackQCompat: TypeAlias = Literal[Interest.CALLBACK_QUERY]


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


MessageComb: TypeAlias = InterestCombinator[MessageCompat, Message]
CallbackQComb: TypeAlias = InterestCombinator[CallbackQCompat, CallbackQuery]

message = MessageComb({Interest.MESSAGE})
edited_message = MessageComb({Interest.EDITED_MESSAGE})
callback_query = CallbackQComb({Interest.CALLBACK_QUERY})


__all__ = [
    "InterestCombinator",
    "InterestedHandler",
    #
    # Combinators
    "message",
    "edited_message",
]
