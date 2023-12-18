# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-18 07:44:15.244650
from dataclasses import dataclass
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class DeleteStickerFromSet:
    """Use this method to delete a sticker from a set created by the bot. Returns True on success."""

    sticker: str
    """File identifier of the sticker """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["DeleteStickerFromSet"]
