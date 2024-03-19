"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class ForumTopicClosed:
    """This object represents a service message about a forum topic closed in
    the chat. Currently holds no information.  Telegram documentation:
    https://core.telegram.org/bots/api#forumtopicclosed"""

    def alter(self) -> ForumTopicClosed:
        return ForumTopicClosed()


__all__ = ["ForumTopicClosed"]
