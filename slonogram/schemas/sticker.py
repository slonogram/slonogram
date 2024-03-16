from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    photo_size as _photo_size,
    mask_position as _mask_position,
    file as _file,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Sticker:
    """This object represents a sticker.
    Telegram docs: https://core.telegram.org/bots/api#sticker"""

    custom_emoji_id: str
    """ Optional. For custom emoji stickers, unique identifier of the custom emoji """
    emoji: str
    """ Optional. Emoji associated with the sticker """
    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_size: int
    """ Optional. File size in bytes """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    height: int
    """ Sticker height """
    is_animated: bool
    """ True, if the sticker is animated """
    is_video: bool
    """ True, if the sticker is a video sticker """
    mask_position: _mask_position.MaskPosition
    """ Optional. For mask stickers, the position where the mask should be placed """
    needs_repainting: bool
    """ Optional. True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places """
    premium_animation: _file.File
    """ Optional. For premium regular stickers, premium animation for the sticker """
    set_name: str
    """ Optional. Name of the sticker set to which the sticker belongs """
    thumbnail: _photo_size.PhotoSize
    """ Optional. Sticker thumbnail in the .WEBP or .JPG format """
    type: str
    """ Type of the sticker, currently one of "regular", "mask", "custom_emoji". The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video. """
    width: int
    """ Sticker width """

    def alter(
        self,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        height: Omittable[Alterer1[int]] = OMIT,
        is_animated: Omittable[Alterer1[bool]] = OMIT,
        is_video: Omittable[Alterer1[bool]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        width: Omittable[Alterer1[int]] = OMIT,
        custom_emoji_id: Omittable[Alterer1[str]] = OMIT,
        emoji: Omittable[Alterer1[str]] = OMIT,
        file_size: Omittable[Alterer1[int]] = OMIT,
        mask_position: Omittable[Alterer1[_mask_position.MaskPosition]] = OMIT,
        needs_repainting: Omittable[Alterer1[bool]] = OMIT,
        premium_animation: Omittable[Alterer1[_file.File]] = OMIT,
        set_name: Omittable[Alterer1[str]] = OMIT,
        thumbnail: Omittable[Alterer1[_photo_size.PhotoSize]] = OMIT,
    ) -> Sticker:
        return Sticker(
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            height=alter1(height, self.height),
            is_animated=alter1(is_animated, self.is_animated),
            is_video=alter1(is_video, self.is_video),
            type=alter1(type, self.type),
            width=alter1(width, self.width),
            custom_emoji_id=alter1(custom_emoji_id, self.custom_emoji_id),
            emoji=alter1(emoji, self.emoji),
            file_size=alter1(file_size, self.file_size),
            mask_position=alter1(mask_position, self.mask_position),
            needs_repainting=alter1(needs_repainting, self.needs_repainting),
            premium_animation=alter1(premium_animation, self.premium_animation),
            set_name=alter1(set_name, self.set_name),
            thumbnail=alter1(thumbnail, self.thumbnail),
        )


__all__ = ["Sticker"]
