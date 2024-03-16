from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class VideoChatScheduled:
    start_date: int
    """ Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator """

    def alter(self, start_date: Omittable[Alterer1[int]] = OMIT):
        return VideoChatScheduled(
            start_date=alter1(start_date, self.start_date),
        )


__all__ = ["VideoChatScheduled"]
