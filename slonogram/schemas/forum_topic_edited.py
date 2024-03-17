from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ForumTopicEdited:
    """This object represents a service message about an edited forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicedited"""

    icon_custom_emoji_id: str | None = None
    """ Optional. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed """
    name: str | None = None
    """ Optional. New name of the topic, if it was edited """

    def alter(
        self,
        icon_custom_emoji_id: Omittable[Alterer1[str | None]] = OMIT,
        name: Omittable[Alterer1[str | None]] = OMIT,
    ) -> ForumTopicEdited:
        return ForumTopicEdited(
            icon_custom_emoji_id=alter1(
                icon_custom_emoji_id, self.icon_custom_emoji_id
            ),
            name=alter1(name, self.name),
        )


__all__ = ["ForumTopicEdited"]
