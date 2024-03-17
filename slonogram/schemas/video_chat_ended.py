from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class VideoChatEnded:
    """This object represents a service message about a video chat ended in the chat.

    Telegram documentation: https://core.telegram.org/bots/api#videochatended"""

    duration: int
    """ Video chat duration in seconds """

    def alter(self, duration: Omittable[Alterer1[int]] = OMIT) -> VideoChatEnded:
        return VideoChatEnded(
            duration=alter1(duration, self.duration),
        )


__all__ = ["VideoChatEnded"]
