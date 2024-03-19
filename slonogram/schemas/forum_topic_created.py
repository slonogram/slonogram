"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class ForumTopicCreated:
    """This object represents a service message about a new forum topic
    created in the chat.  Telegram documentation:
    https://core.telegram.org/bots/api#forumtopiccreated"""

    icon_color: int
    """Color of the topic icon in RGB format"""
    name: str
    """Name of the topic"""
    icon_custom_emoji_id: str | None = None
    """Optional. Unique identifier of the custom emoji shown as the topic
    icon"""

    def alter(
        self,
        icon_color: Omittable[Alterer1[int]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
        icon_custom_emoji_id: Omittable[Alterer1[str | None]] = OMIT,
    ) -> ForumTopicCreated:
        return ForumTopicCreated(
            icon_color=alter1(icon_color, self.icon_color),
            name=alter1(name, self.name),
            icon_custom_emoji_id=alter1(
                icon_custom_emoji_id, self.icon_custom_emoji_id
            ),
        )


__all__ = ["ForumTopicCreated"]
