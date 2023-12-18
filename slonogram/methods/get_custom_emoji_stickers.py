# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class GetCustomEmojiStickers:
    """Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects."""

    custom_emoji_ids: list[str]
    """List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["GetCustomEmojiStickers"]
