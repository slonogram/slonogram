# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class SetCustomEmojiStickerSetThumbnail:
    """Use this method to set the thumbnail of a custom emoji sticker set. Returns True on success."""

    name: str
    """Sticker set name """
    custom_emoji_id: str | None = None
    """Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail. """


__all__ = ["SetCustomEmojiStickerSetThumbnail"]
