# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-17 15:06:50.427429
from dataclasses import dataclass
from slonogram.schemas import MaskPosition
from io import IOBase
from slonogram._internal.utils import collect_attachs_from


@dataclass(frozen=False, slots=True)
class SetStickerMaskPosition:
    """Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns True on success."""

    sticker: str
    """File identifier of the sticker """
    mask_position: MaskPosition | None = None
    """A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position. """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        pass


__all__ = ["SetStickerMaskPosition"]
