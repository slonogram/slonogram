"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import chat as _chat
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class Story:
    """This object represents a story.  Telegram documentation:
    https://core.telegram.org/bots/api#story"""

    chat: _chat.Chat
    """Chat that posted the story"""
    id: int
    """Unique identifier for the story in the chat"""

    def alter(
        self,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        id: Omittable[Alterer1[int]] = OMIT,
    ) -> Story:
        return Story(
            chat=alter1(chat, self.chat),
            id=alter1(id, self.id),
        )


__all__ = ["Story"]
