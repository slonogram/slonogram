from __future__ import annotations
from slonogram.schemas import chat as _chat, chat_boost_source as _chat_boost_source
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ChatBoostRemoved:
    """This object represents a boost removed from a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostremoved"""

    boost_id: str
    """ Unique identifier of the boost """
    chat: _chat.Chat
    """ Chat which was boosted """
    remove_date: int
    """ Point in time (Unix timestamp) when the boost was removed """
    source: _chat_boost_source.ChatBoostSource
    """ Source of the removed boost """

    def alter(
        self,
        boost_id: Omittable[Alterer1[str]] = OMIT,
        chat: Omittable[Alterer1[_chat.Chat]] = OMIT,
        remove_date: Omittable[Alterer1[int]] = OMIT,
        source: Omittable[Alterer1[_chat_boost_source.ChatBoostSource]] = OMIT,
    ) -> ChatBoostRemoved:
        return ChatBoostRemoved(
            boost_id=alter1(boost_id, self.boost_id),
            chat=alter1(chat, self.chat),
            remove_date=alter1(remove_date, self.remove_date),
            source=alter1(source, self.source),
        )


__all__ = ["ChatBoostRemoved"]
