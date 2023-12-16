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
class CreateNewStickerSet:
    """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns True on success."""

    user_id: int
    """User identifier of created sticker set owner """
    name: str
    """Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>". <bot_username> is case insensitive. 1-64 characters. """
    title: str
    """Sticker set title, 1-64 characters """
    stickers: list[InputSticker]
    """A JSON-serialized list of 1-50 initial stickers to be added to the sticker set """
    sticker_format: str
    """Format of stickers in the set, must be one of "static", "animated", "video" """
    sticker_type: str | None = None
    """Type of stickers in the set, pass "regular", "mask", or "custom_emoji". By default, a regular sticker set is created. """
    needs_repainting: bool | None = None
    """Pass True if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only """


__all__ = ["CreateNewStickerSet"]
