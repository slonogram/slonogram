# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class SetChatStickerSet:
    """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""

    chat_id: int | str
    """Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername) """
    sticker_set_name: str
    """Name of the sticker set to be set as the group sticker set """


__all__ = ["SetChatStickerSet"]
