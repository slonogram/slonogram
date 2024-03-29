"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ChatShared:
    """This object contains information about the chat whose identifier was
    shared with the bot using a KeyboardButtonRequestChat button.
    Telegram documentation: https://core.telegram.org/bots/api#chatshared"""

    chat_id: int
    """Identifier of the shared chat. This number may have more than 32
    significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a 64-bit integer or double-precision float type
    are safe for storing this identifier. The bot may not have access to
    the chat and could be unable to use this identifier, unless the chat
    is already known to the bot by some other means."""
    request_id: int
    """Identifier of the request"""

    def alter(
        self,
        chat_id: Omittable[Alterer1[int]] = OMIT,
        request_id: Omittable[Alterer1[int]] = OMIT,
    ) -> ChatShared:
        return ChatShared(
            chat_id=alter1(chat_id, self.chat_id),
            request_id=alter1(request_id, self.request_id),
        )


__all__ = ["ChatShared"]
