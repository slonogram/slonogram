from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class VideoChatScheduled:
    """This object represents a service message about a video chat scheduled in the chat.

    Telegram documentation: https://core.telegram.org/bots/api#videochatscheduled"""

    start_date: int
    """ Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator """

    def alter(self, start_date: Omittable[Alterer1[int]] = OMIT) -> VideoChatScheduled:
        return VideoChatScheduled(
            start_date=alter1(start_date, self.start_date),
        )


__all__ = ["VideoChatScheduled"]
