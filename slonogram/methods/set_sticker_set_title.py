# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class SetStickerSetTitle:
    """Use this method to set the title of a created sticker set. Returns True on success."""

    name: str
    """Sticker set name """
    title: str
    """Sticker set title, 1-64 characters """


__all__ = ["SetStickerSetTitle"]
