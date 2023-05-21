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
    mention = "mention"
    hashtag = "hashtag"
    cashtag = "cashtag"
    bot_command = "bot_command"
    url = "url"
    email = "email"
    phone_number = "phone_number"
    bold = "bold"
    italic = "italic"
    underline = "underline"
    strikethrough = "strikethrough"
    spoiler = "spoiler"
    code = "code"
    pre = "pre"
    text_link = "text_link"
    text_mention = "text_mention"
    custom_emoji = "custom_emoji"


__all__ = ["MessageEntityType", "MessageEntity"]
