from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import photo_size as _photo_size
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class VideoNote:
    """This object represents a video message (available in Telegram apps as of v.4.0).
    Telegram docs: https://core.telegram.org/bots/api#videonote"""

    duration: int
    """ Duration of the video in seconds as defined by sender """
    file_id: str
    """ Identifier for this file, which can be used to download or reuse the file """
    file_size: int
    """ Optional. File size in bytes """
    file_unique_id: str
    """ Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    length: int
    """ Video width and height (diameter of the video message) as defined by sender """
    thumbnail: _photo_size.PhotoSize
    """ Optional. Video thumbnail """

    def alter(
        self,
        duration: Omittable[Alterer1[int]] = OMIT,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        length: Omittable[Alterer1[int]] = OMIT,
        file_size: Omittable[Alterer1[int]] = OMIT,
        thumbnail: Omittable[Alterer1[_photo_size.PhotoSize]] = OMIT,
    ):
        return VideoNote(
            duration=alter1(duration, self.duration),
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            length=alter1(length, self.length),
            file_size=alter1(file_size, self.file_size),
            thumbnail=alter1(thumbnail, self.thumbnail),
        )


__all__ = ["VideoNote"]
