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
class SetChatAdministratorCustomTitle:
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    user_id: int
    """Unique identifier of the target user """
    custom_title: str
    """New custom title for the administrator; 0-16 characters, emoji are not allowed """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["SetChatAdministratorCustomTitle"]
