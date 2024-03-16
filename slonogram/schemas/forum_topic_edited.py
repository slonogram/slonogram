from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ForumTopicEdited:
    """This object represents a service message about an edited forum topic.
    Telegram docs: https://core.telegram.org/bots/api#forumtopicedited"""

    icon_custom_emoji_id: str
    """ Optional. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed """
    name: str
    """ Optional. New name of the topic, if it was edited """

    def alter(
        self,
        icon_custom_emoji_id: Omittable[Alterer1[str]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
    ):
        return ForumTopicEdited(
            icon_custom_emoji_id=alter1(
                icon_custom_emoji_id, self.icon_custom_emoji_id
            ),
            name=alter1(name, self.name),
        )


__all__ = ["ForumTopicEdited"]
