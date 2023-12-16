# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetCustomEmojiStickers:
    """Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects."""

    custom_emoji_ids: list[str]
    """List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified. """


__all__ = ["GetCustomEmojiStickers"]
