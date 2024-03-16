from __future__ import annotations
from slonogram._internal.utils import model


@model
class GeneralForumTopicUnhidden:
    """This object represents a service message about General forum topic unhidden in the chat. Currently holds no information.
    Telegram docs: https://core.telegram.org/bots/api#generalforumtopicunhidden"""

    def alter(self) -> GeneralForumTopicUnhidden:
        return GeneralForumTopicUnhidden()


__all__ = ["GeneralForumTopicUnhidden"]
