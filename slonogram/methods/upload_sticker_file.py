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
class UploadStickerFile:
    """Use this method to upload a file with a sticker for later use in the createNewStickerSet and addStickerToSet methods (the file can be used multiple times). Returns the uploaded File on success."""

    user_id: int
    """User identifier of sticker file owner """
    sticker: IOBase
    """A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See https://core.telegram.org/stickers for technical requirements. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """
    sticker_format: str
    """Format of the sticker, must be one of "static", "animated", "video" """

    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        if isinstance(self.sticker, IOBase):
            dest[str(id(self.sticker))] = self.sticker


__all__ = ["UploadStickerFile"]
