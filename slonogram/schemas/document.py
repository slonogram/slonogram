from __future__ import annotations
from slonogram.schemas import photo_size as _photo_size
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class Document:
    """This object represents a general file (as opposed to photos, voice messages and audio files).

    Telegram documentation: https://core.telegram.org/bots/api#document"""

    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    file_name: str | None = None
    """ Optional. Original filename as defined by sender """
    file_size: int | None = None
    """ Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """
    mime_type: str | None = None
    """ Optional. MIME type of the file as defined by sender """
    thumbnail: _photo_size.PhotoSize | None = None
    """ Optional. Document thumbnail as defined by sender """

    def alter(
        self,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        file_name: Omittable[Alterer1[str | None]] = OMIT,
        file_size: Omittable[Alterer1[int | None]] = OMIT,
        mime_type: Omittable[Alterer1[str | None]] = OMIT,
        thumbnail: Omittable[Alterer1[_photo_size.PhotoSize | None]] = OMIT,
    ) -> Document:
        return Document(
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            file_name=alter1(file_name, self.file_name),
            file_size=alter1(file_size, self.file_size),
            mime_type=alter1(mime_type, self.mime_type),
            thumbnail=alter1(thumbnail, self.thumbnail),
        )


__all__ = ["Document"]
