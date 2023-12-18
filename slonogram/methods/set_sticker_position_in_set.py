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
class SetStickerPositionInSet:
    """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success."""

    sticker: str
    """File identifier of the sticker """
    position: int
    """New sticker position in the set, zero-based """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["SetStickerPositionInSet"]
