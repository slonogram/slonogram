from typing import Optional
from dataclasses import dataclass

from .user import User
from .chat import Message


@dataclass
class CallbackGame:
    pass


@dataclass
class CallbackQuery:
    id: str
    from_: User
    chat_instance: str

    message: Optional[Message] = None
    inline_message_id: Optional[str] = None
    data: Optional[str] = None
    game_short_name: Optional[str] = None


@dataclass
class SwitchInlineQueryChosenChat:
    query: Optional[str] = None

    allow_user_chats: Optional[bool] = None
    allow_bot_chats: Optional[bool] = None
    allow_group_chats: Optional[bool] = None
    allow_channel_chats: Optional[bool] = None
