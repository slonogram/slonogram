from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ForumTopic:
    icon_color: int
    """ Color of the topic icon in RGB format """
    icon_custom_emoji_id: str
    """ Optional. Unique identifier of the custom emoji shown as the topic icon """
    message_thread_id: int
    """ Unique identifier of the forum topic """
    name: str
    """ Name of the topic """

    def alter(
        self,
        icon_color: Omittable[Alterer1[int]] = OMIT,
        message_thread_id: Omittable[Alterer1[int]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
        icon_custom_emoji_id: Omittable[Alterer1[str]] = OMIT,
    ):
        return ForumTopic(
            icon_color=alter1(icon_color, self.icon_color),
            message_thread_id=alter1(message_thread_id, self.message_thread_id),
            name=alter1(name, self.name),
            icon_custom_emoji_id=alter1(
                icon_custom_emoji_id, self.icon_custom_emoji_id
            ),
        )


__all__ = ["ForumTopic"]
