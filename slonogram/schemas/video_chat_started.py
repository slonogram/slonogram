from __future__ import annotations
from slonogram._internal.utils import model


@model
class VideoChatStarted:
    def alter(self):
        return VideoChatStarted()


__all__ = ["VideoChatStarted"]
