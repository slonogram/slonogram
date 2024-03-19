from enum import StrEnum, auto

class Interest(StrEnum):
    MESSAGE = auto()
    EDITED_MESSAGE = auto()
    CHANNEL_POST = auto()
    EDITED_CHANNEL_POST = auto()
    MESSAGE_REACTION = auto()
    MESSAGE_REACTION_COUNT = auto()
    INLINE_QUERY = auto()
    CHOSEN_INLINE_QUERY = auto()
    CALLBACK_QUERY = auto()
    SHIPPING_QUERY = auto()
    PRE_CHECKOUT_QUERY = auto()
    POLL = auto()
    POLL_ANSWER = auto()
    MY_CHAT_MEMBER = auto()
    CHAT_MEMBER = auto()
    CHAT_JOIN_REQUEST = auto()
    CHAT_BOOST = auto()
    REMOVED_CHAT_BOOST = auto()


__all__ = ["Interest"]
