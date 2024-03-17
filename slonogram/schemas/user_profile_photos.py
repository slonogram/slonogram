from __future__ import annotations
from slonogram.schemas import photo_size as _photo_size
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class UserProfilePhotos:
    """This object represent a user's profile pictures.

    Telegram documentation: https://core.telegram.org/bots/api#userprofilephotos"""

    photos: tuple[tuple[_photo_size.PhotoSize, ...], ...]
    """ Requested profile pictures (in up to 4 sizes each) """
    total_count: int
    """ Total number of profile pictures the target user has """

    def alter(
        self,
        photos: Omittable[
            Alterer1[tuple[tuple[_photo_size.PhotoSize, ...], ...]]
        ] = OMIT,
        total_count: Omittable[Alterer1[int]] = OMIT,
    ) -> UserProfilePhotos:
        return UserProfilePhotos(
            photos=alter1(photos, self.photos),
            total_count=alter1(total_count, self.total_count),
        )


__all__ = ["UserProfilePhotos"]
