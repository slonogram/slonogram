from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail.

    Telegram documentation: https://core.telegram.org/bots/api#photosize"""

    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    height: int
    """ Photo height """
    width: int
    """ Photo width """
    file_size: int | None = None
    """ Optional. File size in bytes """

    def alter(
        self,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        height: Omittable[Alterer1[int]] = OMIT,
        width: Omittable[Alterer1[int]] = OMIT,
        file_size: Omittable[Alterer1[int | None]] = OMIT,
    ) -> PhotoSize:
        return PhotoSize(
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            height=alter1(height, self.height),
            width=alter1(width, self.width),
            file_size=alter1(file_size, self.file_size),
        )


__all__ = ["PhotoSize"]
