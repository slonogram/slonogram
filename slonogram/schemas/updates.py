from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .chat import Message


class UpdateType(str, Enum):
    message = "message"
    edited_message = "edited_message"
    channel_post = "channel_post"
    edited_channel_post = "edited_channel_post"
    inline_query = "inline_query"
    chosen_inline_result = "chosen_inline_result"
    callback_query = "callback_query"
    shipping_query = "shipping_query"
    pre_checkout_query = "pre_checkout_query"
    poll = "poll"
    poll_answer = "poll_answer"

    chat_member = "chat_member"
    chat_join_request = "chat_join_request"


@dataclass(slots=True)
class Update:
    id: int

    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None


__all__ = ["Update", "UpdateType"]
