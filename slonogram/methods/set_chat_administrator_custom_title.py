# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class SetChatAdministratorCustomTitle:
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    user_id: int
    """Unique identifier of the target user """
    custom_title: str
    """New custom title for the administrator; 0-16 characters, emoji are not allowed """


__all__ = ["SetChatAdministratorCustomTitle"]
