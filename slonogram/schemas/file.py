"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class File:
    """This object represents a file ready to be downloaded. The file can be
    downloaded via the link
    https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed
    that the link will be valid for at least 1 hour. When the link
    expires, a new one can be requested by calling getFile.  Telegram
    documentation: https://core.telegram.org/bots/api#file"""

    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    file_path: str | None = None
    """Optional. File path. Use
    https://api.telegram.org/file/bot<token>/<file_path> to get the file."""
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""

    def alter(
        self,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        file_path: Omittable[Alterer1[str | None]] = OMIT,
        file_size: Omittable[Alterer1[int | None]] = OMIT,
    ) -> File:
        return File(
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            file_path=alter1(file_path, self.file_path),
            file_size=alter1(file_size, self.file_size),
        )


__all__ = ["File"]
