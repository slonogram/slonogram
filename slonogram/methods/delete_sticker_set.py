# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 15:06:50.427429
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class DeleteStickerSet:
    """Use this method to delete a sticker set that was created by the bot. Returns True on success."""

    name: str
    """Sticker set name """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["DeleteStickerSet"]
