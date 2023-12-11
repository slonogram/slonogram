from enum import StrEnum, auto
from typing import Literal, TypeAlias


class Interest(StrEnum):
    MESSAGE = auto()
    EDITED_MESSAGE = auto()
    CHANNEL_POST = auto()
    EDITED_CHANNEL_POST = auto()
    INLINE_QUERY = auto()
    CHOSEN_INLINE_RESULT = auto()
    CALLBACK_QUERY = auto()
    SHIPPING_QUERY = auto()
    PRE_CHECKOUT_QUERY = auto()
    POLL = auto()
    POLL_ANSWER = auto()
    MY_CHAT_MEMBER = auto()
    CHAT_MEMBER = auto()
    CHAT_JOIN_REQUEST = auto()


# fmt: off
MessageI: TypeAlias            = Literal[Interest.MESSAGE]
EditedMessageI: TypeAlias      = Literal[Interest.EDITED_MESSAGE]
ChannelPostI: TypeAlias        = Literal[Interest.CHANNEL_POST]
EditedChannelPostI: TypeAlias  = Literal[Interest.EDITED_CHANNEL_POST]
InlineQueryI: TypeAlias        = Literal[Interest.INLINE_QUERY]
ChosenInlineResultI: TypeAlias = Literal[Interest.CHOSEN_INLINE_RESULT]
CallbackQueryI: TypeAlias      = Literal[Interest.CALLBACK_QUERY]
ShippingQueryI: TypeAlias      = Literal[Interest.SHIPPING_QUERY]
PreCheckoutQueryI: TypeAlias   = Literal[Interest.PRE_CHECKOUT_QUERY]
PollI: TypeAlias               = Literal[Interest.POLL]
PollAnswerI: TypeAlias         = Literal[Interest.POLL_ANSWER]
MyChatMemberI: TypeAlias       = Literal[Interest.MY_CHAT_MEMBER]
ChatMemberI: TypeAlias         = Literal[Interest.CHAT_MEMBER]
ChatJoinRequestI: TypeAlias    = Literal[Interest.CHAT_JOIN_REQUEST]
# fmt: on
