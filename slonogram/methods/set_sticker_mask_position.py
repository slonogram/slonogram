# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
# Generated at: 2023-12-16 11:59:50.816237
from dataclasses import dataclass
from slonogram.schemas import MaskPosition


@dataclass(frozen=False, slots=True)
class SetStickerMaskPosition:
    """Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns True on success."""

    sticker: str
    """File identifier of the sticker """
    mask_position: MaskPosition | None = None
    """A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position. """


__all__ = ["SetStickerMaskPosition"]
