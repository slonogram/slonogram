from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class PhotoSize:
    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_size: int
    """ Optional. File size in bytes """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    height: int
    """ Photo height """
    width: int
    """ Photo width """

    def alter(
        self,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        height: Omittable[Alterer1[int]] = OMIT,
        width: Omittable[Alterer1[int]] = OMIT,
        file_size: Omittable[Alterer1[int]] = OMIT,
    ):
        return PhotoSize(
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            height=alter1(height, self.height),
            width=alter1(width, self.width),
            file_size=alter1(file_size, self.file_size),
        )


__all__ = ["PhotoSize"]
