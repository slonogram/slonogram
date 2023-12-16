# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import InputSticker


@dataclass(frozen=False, slots=True)
class AddStickerToSet:
    """Use this method to add a new sticker to a set created by the bot. The format of the added sticker must match the format of the other stickers in the set. Emoji sticker sets can have up to 200 stickers. Animated and video sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success."""

    user_id: int
    """User identifier of sticker set owner """
    name: str
    """Sticker set name """
    sticker: InputSticker
    """A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn't changed. """


__all__ = ["AddStickerToSet"]
