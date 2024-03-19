"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import chat_boost as _chat_boost, chat as _chat
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ChatBoostUpdated:
    """This object represents a boost added to a chat or changed.  Telegram
    documentation: https://core.telegram.org/bots/api#chatboostupdated"""

    boost: _chat_boost.ChatBoost
    """Information about the chat boost"""
    chat: _chat.Chat
    """Chat which was boosted"""

    def alter(
        self,
        boost: Omittable[Alterer1[_chat_boost.ChatBoost]] = OMIT,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
    ) -> ChatBoostUpdated:
        return ChatBoostUpdated(
            boost=alter1(boost, self.boost),
            chat=alter1(chat, self.chat),
        )


__all__ = ["ChatBoostUpdated"]
