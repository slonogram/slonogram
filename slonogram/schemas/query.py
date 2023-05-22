from typing import Optional
from dataclasses import dataclass

from .user import User
from .chat import Message, ChatType, Location


@dataclass(slots=True)
class InlineQuery:
    id: str
    from_: User
    query: str
    offset: str

    chat_type: Optional[ChatType] = None
    location: Optional[Location] = None


@dataclass(slots=True)
class CallbackQuery:
    id: str
    from_: User
    chat_instance: str

    message: Optional[Message] = None
    inline_message_id: Optional[str] = None
    data: Optional[str] = None
    game_short_name: Optional[str] = None


__slots__ = ["CallbackQuery"]
