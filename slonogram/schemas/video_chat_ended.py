from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class VideoChatEnded:
    duration: int
    """ Video chat duration in seconds """

    def alter(self, duration: Omittable[Alterer1[int]] = OMIT):
        return VideoChatEnded(
            duration=alter1(duration, self.duration),
        )


__all__ = ["VideoChatEnded"]
