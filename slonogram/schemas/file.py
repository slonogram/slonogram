from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.
    Telegram docs: https://core.telegram.org/bots/api#file"""

    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_path: str
    """ Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file. """
    file_size: int
    """ Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """

    def alter(
        self,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        file_path: Omittable[Alterer1[str]] = OMIT,
        file_size: Omittable[Alterer1[int]] = OMIT,
    ) -> File:
        return File(
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            file_path=alter1(file_path, self.file_path),
            file_size=alter1(file_size, self.file_size),
        )


__all__ = ["File"]
