# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 15:47:05.015225
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SetChatPhoto:
    """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target channel (in the format @channelusername) """
    photo: IOBase
    """New chat photo, uploaded using multipart/form-data """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.photo, IOBase):
            dest[str(id(self.photo))] = self.photo


__all__ = ["SetChatPhoto"]
