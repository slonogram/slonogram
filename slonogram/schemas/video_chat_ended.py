from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class VideoChatEnded:
    """This object represents a service message about a video chat ended in the chat.
    Telegram docs: https://core.telegram.org/bots/api#videochatended"""

    duration: int
    """ Video chat duration in seconds """

    def alter(self, duration: Omittable[Alterer1[int]] = OMIT) -> VideoChatEnded:
        return VideoChatEnded(
            duration=alter1(duration, self.duration),
        )


__all__ = ["VideoChatEnded"]
