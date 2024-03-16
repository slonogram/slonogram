from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class MessageId:
    """This object represents a unique message identifier.
    Telegram docs: https://core.telegram.org/bots/api#messageid"""

    message_id: int
    """ Unique message identifier """

    def alter(self, message_id: Omittable[Alterer1[int]] = OMIT):
        return MessageId(
            message_id=alter1(message_id, self.message_id),
        )


__all__ = ["MessageId"]
