# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-18 07:44:15.244650
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class EditGeneralForumTopic:
    """Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    name: str
    """New topic name, 1-128 characters """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["EditGeneralForumTopic"]
