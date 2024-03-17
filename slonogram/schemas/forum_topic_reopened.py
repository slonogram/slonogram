from __future__ import annotations
from slonogram._internal.utils import model


@model
class ForumTopicReopened:
    """This object represents a service message about a forum topic reopened in the chat. Currently holds no information.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicreopened"""

    def alter(self) -> ForumTopicReopened:
        return ForumTopicReopened()


__all__ = ["ForumTopicReopened"]
