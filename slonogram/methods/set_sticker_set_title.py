# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 15:47:05.015225
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SetStickerSetTitle:
    """Use this method to set the title of a created sticker set. Returns True on success."""

    name: str
    """Sticker set name """
    title: str
    """Sticker set title, 1-64 characters """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["SetStickerSetTitle"]
