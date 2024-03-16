from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import photo_size as _photo_size, sticker as _sticker
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class StickerSet:
    is_animated: bool
    """ True, if the sticker set contains animated stickers """
    is_video: bool
    """ True, if the sticker set contains video stickers """
    name: str
    """ Sticker set name """
    sticker_type: str
    """ Type of stickers in the set, currently one of "regular", "mask", "custom_emoji" """
    stickers: list[_sticker.Sticker]
    """ List of all set stickers """
    thumbnail: _photo_size.PhotoSize
    """ Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format """
    title: str
    """ Sticker set title """

    def alter(
        self,
        is_animated: Omittable[Alterer1[bool]] = OMIT,
        is_video: Omittable[Alterer1[bool]] = OMIT,
        name: Omittable[Alterer1[str]] = OMIT,
        sticker_type: Omittable[Alterer1[str]] = OMIT,
        stickers: Omittable[Alterer1[list[_sticker.Sticker]]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        thumbnail: Omittable[Alterer1[_photo_size.PhotoSize]] = OMIT,
    ):
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
