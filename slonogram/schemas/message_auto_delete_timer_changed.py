from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class MessageAutoDeleteTimerChanged:
    message_auto_delete_time: int
    """ New auto-delete time for messages in the chat; in seconds """

    def alter(self, message_auto_delete_time: Omittable[Alterer1[int]] = OMIT):
        return MessageAutoDeleteTimerChanged(
            message_auto_delete_time=alter1(
                message_auto_delete_time, self.message_auto_delete_time
            ),
        )


__all__ = ["MessageAutoDeleteTimerChanged"]
