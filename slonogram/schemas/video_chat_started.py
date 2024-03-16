from __future__ import annotations
from slonogram._internal.utils import model


@model
class VideoChatStarted:
    """This object represents a service message about a video chat started in the chat. Currently holds no information.
    Telegram docs: https://core.telegram.org/bots/api#videochatstarted"""

    def alter(self):
        return VideoChatStarted()


__all__ = ["VideoChatStarted"]