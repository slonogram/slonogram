# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass


@dataclass(frozen=False, slots=True)
class GetStickerSet:
    """Use this method to get a sticker set. On success, a StickerSet object is returned."""

    name: str
    """Name of the sticker set """


__all__ = ["GetStickerSet"]
