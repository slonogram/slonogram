from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ChatBoostAdded:
    """This object represents a service message about a user boosting a chat.

    Telegram documentation: https://core.telegram.org/bots/api#chatboostadded"""

    boost_count: int
    """ Number of boosts added by the user """

    def alter(self, boost_count: Omittable[Alterer1[int]] = OMIT) -> ChatBoostAdded:
        return ChatBoostAdded(
            boost_count=alter1(boost_count, self.boost_count),
        )


__all__ = ["ChatBoostAdded"]
