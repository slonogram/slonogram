from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class MessageAutoDeleteTimerChanged:
    """This object represents a service message about a change in auto-delete timer settings.

    Telegram documentation: https://core.telegram.org/bots/api#messageautodeletetimerchanged"""

    message_auto_delete_time: int
    """ New auto-delete time for messages in the chat; in seconds """

    def alter(
        self, message_auto_delete_time: Omittable[Alterer1[int]] = OMIT
    ) -> MessageAutoDeleteTimerChanged:
        return MessageAutoDeleteTimerChanged(
            message_auto_delete_time=alter1(
                message_auto_delete_time, self.message_auto_delete_time
            ),
        )


__all__ = ["MessageAutoDeleteTimerChanged"]
