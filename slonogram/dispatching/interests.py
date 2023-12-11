from __future__ import annotations
from typing import (
    TypeVar,
    Generic,
    TypeAlias,
    cast,
    Any,
)


from ..schemas import Message, CallbackQuery, InlineQuery

from ..types import interest as I
from ..types.interest import Interest


C = TypeVar("C", contravariant=True)
M = TypeVar("M", covariant=True)
T = TypeVar("T")

MessageCompat: TypeAlias = I.MessageI | I.EditedMessageI
CallbackQCompat: TypeAlias = I.CallbackQueryI
InlineQCompat: TypeAlias = I.InlineQueryI

RelaxedCompat: TypeAlias = Interest


class InterestCombinator(Generic[C, M]):
    __slots__ = ("interests",)

    def __init__(self, interests: set[Interest]) -> None:
        self.interests = interests

    def yield_if(self, interest: Interest, item: T) -> tuple[T] | tuple[()]:
        if interest in self.interests:
            return (item,)
        return ()

    def __or__(
        self,
        rhs: InterestCombinator[C, M],
    ) -> InterestCombinator[C, M]:
        return InterestCombinator[C, M]({*self.interests, *rhs.interests})


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
