"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class ForumTopicReopened:
    """This object represents a service message about a forum topic reopened
    in the chat. Currently holds no information.  Telegram documentation:
    https://core.telegram.org/bots/api#forumtopicreopened"""

    def alter(self) -> ForumTopicReopened:
        return ForumTopicReopened()


__all__ = ["ForumTopicReopened"]
