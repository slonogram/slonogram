from __future__ import annotations
from slonogram._internal.utils import model


@model
class GeneralForumTopicHidden:
    """This object represents a service message about General forum topic hidden in the chat. Currently holds no information.
    Telegram docs: https://core.telegram.org/bots/api#generalforumtopichidden"""

    def alter(self):
        return GeneralForumTopicHidden()


__all__ = ["GeneralForumTopicHidden"]
