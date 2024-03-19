"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import sticker as _sticker, photo_size as _photo_size
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class StickerSet:
    """This object represents a sticker set.  Telegram documentation:
    https://core.telegram.org/bots/api#stickerset"""

    is_animated: bool
    """True, if the sticker set contains animated stickers"""
    is_video: bool
    """True, if the sticker set contains video stickers"""
    name: str
    """Sticker set name"""
    sticker_type: str
    """Type of stickers in the set, currently one of "regular", "mask",
    "custom_emoji" """
    stickers: tuple[_sticker.Sticker, ...]
    """List of all set stickers"""
    title: str
    """Sticker set title"""
    thumbnail: _photo_size.PhotoSize | None = None
    """Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format"""

    def alter(
        self,
        is_animated: Omittable[Alterer1[bool]] = OMIT,
        is_video: Omittable[Alterer1[bool]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
        sticker_type: Omittable[Alterer1[str]] = OMIT,
        stickers: Omittable[Alterer1[tuple[_sticker.Sticker, ...]]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        thumbnail: Omittable[Alterer1[_photo_size.PhotoSize | None]] = OMIT,
    ) -> StickerSet:
        return StickerSet(
            is_animated=alter1(is_animated, self.is_animated),
            is_video=alter1(is_video, self.is_video),
            name=alter1(name, self.name),
            sticker_type=alter1(sticker_type, self.sticker_type),
            stickers=alter1(stickers, self.stickers),
            title=alter1(title, self.title),
            thumbnail=alter1(thumbnail, self.thumbnail),
        )


__all__ = ["StickerSet"]
