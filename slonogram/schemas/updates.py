from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .chat import Message


class UpdateType(str, Enum):
    MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    CHANNEL_POST = "channel_post"
    EDITED_CHANNEL_POST = "edited_channel_post"
    INLINE_QUERY = "inline_query"
    CHOSEN_INLINE_RESULT = "chosen_inline_result"
    CALLBACK_QUERY = "callback_query"
    SHIPPING_QUERY = "shipping_query"
    PRE_CHECKOUT_QUERY = "pre_checkout_query"
    POLL = "poll"
    POLL_ANSWER = "poll_answer"

    CHAT_MEMBER = "chat_member"
    CHAT_JOIN_REQUEST = "chat_join_request"


@dataclass(slots=True)
class Update:
    id: int

    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None


__all__ = ["Update", "UpdateType"]
