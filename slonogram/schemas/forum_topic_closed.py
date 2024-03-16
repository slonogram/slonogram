from __future__ import annotations
from slonogram._internal.utils import model


@model
class ForumTopicClosed:
    """This object represents a service message about a forum topic closed in the chat. Currently holds no information.
    Telegram docs: https://core.telegram.org/bots/api#forumtopicclosed"""

    def alter(self) -> ForumTopicClosed:
        return ForumTopicClosed()


__all__ = ["ForumTopicClosed"]
