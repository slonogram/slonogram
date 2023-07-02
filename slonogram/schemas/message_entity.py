from __future__ import annotations
from enum import Enum
from typing import NewType, Optional
from dataclasses import dataclass

from .user import User

Utf16CodeUnits = NewType("Utf16CodeUnits", int)


@dataclass(slots=True)
class MessageEntity:
    type_: MessageEntityType
    offset: Utf16CodeUnits
    length: Utf16CodeUnits

    url: Optional[str] = None
    user: Optional[User] = None
    language: Optional[str] = None
    custom_emoji_id: Optional[str] = None


class MessageEntityType(str, Enum):
    MENTION = "mention"
    HASHTAG = "hashtag"
    CASHTAG = "cashtag"
    BOT_COMMAND = "bot_command"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    SPOILER = "spoiler"
    CODE = "code"
    PRE = "pre"
    TEXT_LINK = "text_link"
    TEXT_MENTION = "text_mention"
    CUSTOM_EMOJI = "custom_emoji"


__all__ = ["MessageEntityType", "MessageEntity", "Utf16CodeUnits"]
