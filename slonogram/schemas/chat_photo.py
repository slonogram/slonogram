from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class ChatPhoto:
    """This object represents a chat photo.

    Telegram documentation: https://core.telegram.org/bots/api#chatphoto"""

    big_file_id: str
    """ File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed. """
    big_file_unique_id: str
    """ Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """
    small_file_id: str
    """ File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed. """
    small_file_unique_id: str
    """ Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. """

    def alter(
        self,
        big_file_id: Omittable[Alterer1[str]] = OMIT,
        big_file_unique_id: Omittable[Alterer1[str]] = OMIT,
        small_file_id: Omittable[Alterer1[str]] = OMIT,
        small_file_unique_id: Omittable[Alterer1[str]] = OMIT,
    ) -> ChatPhoto:
        return ChatPhoto(
            big_file_id=alter1(big_file_id, self.big_file_id),
            big_file_unique_id=alter1(big_file_unique_id, self.big_file_unique_id),
            small_file_id=alter1(small_file_id, self.small_file_id),
            small_file_unique_id=alter1(
                small_file_unique_id, self.small_file_unique_id
            ),
        )


__all__ = ["ChatPhoto"]
