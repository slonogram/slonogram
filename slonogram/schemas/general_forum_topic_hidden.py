"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class GeneralForumTopicHidden:
    """This object represents a service message about General forum topic
    hidden in the chat. Currently holds no information.  Telegram
    documentation:
    https://core.telegram.org/bots/api#generalforumtopichidden"""

    def alter(self) -> GeneralForumTopicHidden:
        return GeneralForumTopicHidden()


__all__ = ["GeneralForumTopicHidden"]
