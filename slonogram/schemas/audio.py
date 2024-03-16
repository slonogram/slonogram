from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import photo_size as _photo_size
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Audio:
    """This object represents an audio file to be treated as music by the Telegram clients.
    Telegram docs: https://core.telegram.org/bots/api#audio"""

    duration: int
    """ Duration of the audio in seconds as defined by sender """
    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_name: str
    """ Optional. Original filename as defined by sender """
    file_size: int
    """ Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    mime_type: str
    """ Optional. MIME type of the file as defined by sender """
    performer: str
    """ Optional. Performer of the audio as defined by sender or by audio tags """
    thumbnail: _photo_size.PhotoSize
    """ Optional. Thumbnail of the album cover to which the music file belongs """
    title: str
    """ Optional. Title of the audio as defined by sender or by audio tags """

    def alter(
        self,
        duration: Omittable[Alterer1[int]] = OMIT,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        file_name: Omittable[Alterer1[str]] = OMIT,
        file_size: Omittable[Alterer1[int]] = OMIT,
        mime_type: Omittable[Alterer1[str]] = OMIT,
        performer: Omittable[Alterer1[str]] = OMIT,
        thumbnail: Omittable[Alterer1[_photo_size.PhotoSize]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
    ) -> Audio:
        return Audio(
            duration=alter1(duration, self.duration),
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            file_name=alter1(file_name, self.file_name),
            file_size=alter1(file_size, self.file_size),
            mime_type=alter1(mime_type, self.mime_type),
            performer=alter1(performer, self.performer),
            thumbnail=alter1(thumbnail, self.thumbnail),
            title=alter1(title, self.title),
        )


__all__ = ["Audio"]
