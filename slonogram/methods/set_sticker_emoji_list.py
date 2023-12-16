# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class SetStickerEmojiList:
    """Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success."""

    sticker: str
    """File identifier of the sticker """
    emoji_list: list[str]
    """A JSON-serialized list of 1-20 emoji associated with the sticker """


__all__ = ["SetStickerEmojiList"]
