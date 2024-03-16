from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat as _chat, chat_boost as _chat_boost
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ChatBoostUpdated:
    """This object represents a boost added to a chat or changed.
    Telegram docs: https://core.telegram.org/bots/api#chatboostupdated"""

    boost: _chat_boost.ChatBoost
    """ Information about the chat boost """
    chat: _chat.Chat
    """ Chat which was boosted """

    def alter(
        self,
        boost: Omittable[Alterer1[_chat_boost.ChatBoost]] = OMIT,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
    ):
        return ChatBoostUpdated(
            boost=alter1(boost, self.boost),
            chat=alter1(chat, self.chat),
        )


__all__ = ["ChatBoostUpdated"]
