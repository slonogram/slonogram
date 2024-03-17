from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ForumTopic:
    """This object represents a forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopic"""

    icon_color: int
    """ Color of the topic icon in RGB format """
    message_thread_id: int
    """ Unique identifier of the forum topic """
    name: str
    """ Name of the topic """
    icon_custom_emoji_id: str | None = None
    """ Optional. Unique identifier of the custom emoji shown as the topic icon """

    def alter(
        self,
        icon_color: Omittable[Alterer1[int]] = OMIT,
        message_thread_id: Omittable[Alterer1[int]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
        icon_custom_emoji_id: Omittable[Alterer1[str | None]] = OMIT,
    ) -> ForumTopic:
        return ForumTopic(
            icon_color=alter1(icon_color, self.icon_color),
            message_thread_id=alter1(message_thread_id, self.message_thread_id),
            name=alter1(name, self.name),
            icon_custom_emoji_id=alter1(
                icon_custom_emoji_id, self.icon_custom_emoji_id
            ),
        )


__all__ = ["ForumTopic"]
