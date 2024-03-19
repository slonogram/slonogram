from typing import (
    TypeVar,
    TypeAlias,
    Iterable,
    reveal_type,
    cast,
    Any,
    TYPE_CHECKING,
)

from .stash import Stash
from .context import Context

from .._internal.interests import collect_interests
from .._internal.utils import flatten
from .._internal.stack import get_caller_module_name

from ..abstract.interested import Interested
from ..types.interest import Interest
from ..middlewares.base import Middlewared
from ..handling.handler import Handler
from ..handling.activation import Activation
from ..omittable import Omittable, omitted_or, OMIT, Omit
from ..altering import alter1, Alterer1

from ..middlewares.only import Only

if TYPE_CHECKING:
    from ..schemas.update import Update
    from ..schemas.maybe_inaccessible_message import Message
    from ..schemas.message_reaction_updated import MessageReactionUpdated
    from ..schemas.message_reaction_count_updated import MessageReactionCountUpdated
    from ..schemas.inline_query import InlineQuery
    from ..schemas.chosen_inline_result import ChosenInlineResult
    from ..schemas.callback_query import CallbackQuery
    from ..schemas.shipping_query import ShippingQuery
    from ..schemas.pre_checkout_query import PreCheckoutQuery
    from ..schemas.poll import Poll
    from ..schemas.poll_answer import PollAnswer
    from ..schemas.chat_member_updated import ChatMemberUpdated
    from ..schemas.chat_join_request import ChatJoinRequest
    from ..schemas.chat_boost_updated import ChatBoostUpdated
    from ..schemas.chat_boost_removed import ChatBoostRemoved

M = TypeVar("M")

_Handlers: TypeAlias = tuple[Handler[M], ...]
_TupOrHandler: TypeAlias = _Handlers[M] | Handler[M]
_MaybeHandlers: TypeAlias = Omittable[_TupOrHandler[M]]

def _into_handler(value: _TupOrHandler[M]) -> Handler[M]:
    if isinstance(value, tuple):
        return Dispatcher(value)
    return value

def _try_flatten(handler: Handler[M]) -> Iterable[Handler[M]]:
    if isinstance(handler, Dispatcher) and handler.mergeable:
        return handler.handlers
    return (handler, )

def _into_handlers(item: _MaybeHandlers[M]) -> Iterable[Handler[M]]:
    if isinstance(item, Omit):
        return ()
    if isinstance(item, tuple):
        return (Dispatcher(item), )
    return (item, )

class Dispatcher(Middlewared[M], Interested):
    __slots__ = (
        "name",
        "stash",
        "handlers",
        "non_mergeable",
    )

    name: str | None
    handlers: _Handlers[M]

    def __init__(
        self,
        handlers: Omittable[_Handlers[M]] = OMIT,
        stash: Omittable[Stash] = OMIT,
        name: Omittable[str | None] = OMIT,
        non_mergeable: Omittable[bool] = OMIT,
    ) -> None:
        self.stash = stash
        self.handlers = omitted_or(handlers, ())
        self.name = omitted_or(name, get_caller_module_name(0))
        self.non_mergeable = omitted_or(non_mergeable, False)
    
    @property
    def mergeable(self) -> bool:
        return not self.non_mergeable and isinstance(self.stash, Omit)

    def alter(
        self,
        handlers: Omittable[Alterer1[_Handlers[M]]] = OMIT,
        stash: Omittable[Alterer1[Omittable[Stash]]] = OMIT,
        name: Omittable[Alterer1[str | None]] = OMIT,
    ) -> "Dispatcher[M]":
        return Dispatcher[M](
            handlers=alter1(handlers, self.handlers),
            stash=alter1(stash, self.stash),
            name=alter1(name, self.name),
        )

    def register(self, *handlers: Handler[M]) -> "Dispatcher[M]":
        return self.alter(handlers=lambda prev: (
            *prev,
            *flatten(map(_try_flatten, handlers))
        ))
    
    def interested(
        self: "Dispatcher[Update]",
        *,
        message: _MaybeHandlers["Message"] = OMIT,
        edited_message: _MaybeHandlers["Message"] = OMIT,
        channel_post: _MaybeHandlers["Message"] = OMIT,
        edited_channel_post: _MaybeHandlers["Message"] = OMIT,

        message_reaction: _MaybeHandlers["MessageReactionUpdated"] = OMIT,
        message_reaction_count: _MaybeHandlers["MessageReactionCountUpdated"] = OMIT,
        inline_query: _MaybeHandlers["InlineQuery"] = OMIT,
        chosen_inline_result: _MaybeHandlers["ChosenInlineResult"] = OMIT,
        callback_query: _MaybeHandlers["CallbackQuery"] = OMIT,
        shipping_query: _MaybeHandlers["ShippingQuery"] = OMIT,
        pre_checkout_query: _MaybeHandlers["PreCheckoutQuery"] = OMIT,
        poll: _MaybeHandlers["Poll"] = OMIT,
        poll_answer: _MaybeHandlers["PollAnswer"] = OMIT,
        my_chat_member: _MaybeHandlers["ChatMemberUpdated"] = OMIT,
        chat_member: _MaybeHandlers["ChatMemberUpdated"] = OMIT,
        chat_join_request: _MaybeHandlers["ChatJoinRequest"] = OMIT,
        chat_boost: _MaybeHandlers["ChatBoostUpdated"] = OMIT,
        removed_chat_boost: _MaybeHandlers["ChatBoostRemoved"] = OMIT,
    ) -> "Dispatcher[Update]":
        handlers_mut: list[Only[Any]] = []
        for interest, _handler in (
            (Interest.MESSAGE, message),
            (Interest.EDITED_MESSAGE, edited_message),
            (Interest.CHANNEL_POST, channel_post),
            (Interest.EDITED_CHANNEL_POST, edited_channel_post),
            (Interest.MESSAGE_REACTION, message_reaction),
            (Interest.MESSAGE_REACTION_COUNT, message_reaction_count),
            (Interest.INLINE_QUERY, inline_query),
            (Interest.CHOSEN_INLINE_QUERY, chosen_inline_result),
            (Interest.CALLBACK_QUERY, callback_query),
            (Interest.SHIPPING_QUERY, shipping_query),
            (Interest.PRE_CHECKOUT_QUERY, pre_checkout_query),
            (Interest.POLL, poll),
            (Interest.POLL_ANSWER, poll_answer),
            (Interest.MY_CHAT_MEMBER, my_chat_member),
            (Interest.CHAT_MEMBER, chat_member),
            (Interest.CHAT_JOIN_REQUEST, chat_join_request),
            (Interest.CHAT_BOOST, chat_boost),
            (Interest.REMOVED_CHAT_BOOST, removed_chat_boost),
        ):
            if isinstance(_handler, Omit):
                continue
            handler = _into_handler(cast(_TupOrHandler[Any], _handler))
            handlers_mut.append(Only(interest, handler))

        handlers = tuple(handlers_mut)
        return self.alter(handlers=lambda prev: (*prev, *handlers))

    def __repr__(self) -> str:
        return f"Dispatcher(name={self.name!r}, handlers={self.handlers})"

    def collect_interests(self) -> set[Interest]:
        return collect_interests(self.handlers)

    async def __call__(
        self,
        context: Context[M],
        /,
    ) -> Activation:
        if not isinstance(self.stash, Omit):
            context = Context(context.bot, context.model, context.stash.append(self.stash))

        for handler in self.handlers:
            print(handler)
            old = context.stash
            context.stash = Stash(old)

            try:
                activation = await handler(context)
            finally:
                context.stash = old

            if activation:
                return activation

        return Activation.stalled()


__all__ = ["Dispatcher"]
