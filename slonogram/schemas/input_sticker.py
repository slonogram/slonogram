from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import mask_position as _mask_position, input_file as _input_file
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class InputSticker:
    """This object describes a sticker to be added to a sticker set.
    Telegram docs: https://core.telegram.org/bots/api#inputsticker"""

    emoji_list: list[str]
    """ List of 1-20 emoji associated with the sticker """
    keywords: list[str]
    """ Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For "regular" and "custom_emoji" stickers only. """
    mask_position: _mask_position.MaskPosition
    """ Optional. Position where the mask should be placed on faces. For "mask" stickers only. """
    sticker: _input_file.InputFile | str
    """ The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, upload a new one using multipart/form-data, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. More information on Sending Files: https://core.telegram.org/bots/api#sending-files """

    def alter(
        self,
        emoji_list: Omittable[Alterer1[list[str]]] = OMIT,
        sticker: Omittable[Alterer1[_input_file.InputFile | str]] = OMIT,
        keywords: Omittable[Alterer1[list[str]]] = OMIT,
        mask_position: Omittable[Alterer1[_mask_position.MaskPosition]] = OMIT,
    ):
        return InputSticker(
            emoji_list=alter1(emoji_list, self.emoji_list),
            sticker=alter1(sticker, self.sticker),
            keywords=alter1(keywords, self.keywords),
            mask_position=alter1(mask_position, self.mask_position),
        )


__all__ = ["InputSticker"]
