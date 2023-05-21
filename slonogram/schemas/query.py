from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

from .user import User
from .chat import Message


@dataclass
class CallbackQuery:
    id: str
    from_: User
    chat_instance: str

    message: Optional[Message] = None
    inline_message_id: Optional[str] = None
    data: Optional[str] = None
    game_short_name: Optional[str] = None
