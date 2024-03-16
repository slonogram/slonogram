from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class PassportFile:
    file_date: int
    """ Unix time when the file was uploaded """
    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_size: int
    """ File size in bytes """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """

    def alter(
        self,
        file_date: Omittable[Alterer1[int]] = OMIT,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_size: Omittable[Alterer1[int]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
    ):
        return PassportFile(
            file_date=alter1(file_date, self.file_date),
            file_id=alter1(file_id, self.file_id),
            file_size=alter1(file_size, self.file_size),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
        )


__all__ = ["PassportFile"]
