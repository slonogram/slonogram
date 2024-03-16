from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat_boost_source as _chat_boost_source
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ChatBoost:
    """This object contains information about a chat boost.
    Telegram docs: https://core.telegram.org/bots/api#chatboost"""

    add_date: int
    """ Point in time (Unix timestamp) when the chat was boosted """
    boost_id: str
    """ Unique identifier of the boost """
    expiration_date: int
    """ Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged """
    source: _chat_boost_source.ChatBoostSource
    """ Source of the added boost """

    def alter(
        self,
        add_date: Omittable[Alterer1[int]] = OMIT,
        boost_id: Omittable[Alterer1[str]] = OMIT,
        expiration_date: Omittable[Alterer1[int]] = OMIT,
        source: Omittable[Alterer1[_chat_boost_source.ChatBoostSource]] = OMIT,
    ) -> ChatBoost:
        return ChatBoost(
            add_date=alter1(add_date, self.add_date),
            boost_id=alter1(boost_id, self.boost_id),
            expiration_date=alter1(expiration_date, self.expiration_date),
            source=alter1(source, self.source),
        )


__all__ = ["ChatBoost"]
