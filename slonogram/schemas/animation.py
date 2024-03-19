"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import photo_size as _photo_size
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class Animation:
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC
    video without sound).  Telegram documentation:
    https://core.telegram.org/bots/api#animation"""

    duration: int
    """Duration of the video in seconds as defined by sender"""
    file_id: str
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    height: int
    """Video height as defined by sender"""
    width: int
    """Video width as defined by sender"""
    file_name: str | None = None
    """Optional. Original animation filename as defined by sender"""
    file_size: int | None = None
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""
    mime_type: str | None = None
    """Optional. MIME type of the file as defined by sender"""
    thumbnail: _photo_size.PhotoSize | None = None
    """Optional. Animation thumbnail as defined by sender"""

    def alter(
        self,
        duration: Omittable[Alterer1[int]] = OMIT,
        file_id: Omittable[Alterer1[str]] = OMIT,
        file_unique_id: Omittable[Alterer1[str]] = OMIT,
        height: Omittable[Alterer1[int]] = OMIT,
        width: Omittable[Alterer1[int]] = OMIT,
        file_name: Omittable[Alterer1[str | None]] = OMIT,
        file_size: Omittable[Alterer1[int | None]] = OMIT,
        mime_type: Omittable[Alterer1[str | None]] = OMIT,
        thumbnail: Omittable[Alterer1[_photo_size.PhotoSize | None]] = OMIT,
    ) -> Animation:
        return Animation(
            duration=alter1(duration, self.duration),
            file_id=alter1(file_id, self.file_id),
            file_unique_id=alter1(file_unique_id, self.file_unique_id),
            height=alter1(height, self.height),
            width=alter1(width, self.width),
            file_name=alter1(file_name, self.file_name),
            file_size=alter1(file_size, self.file_size),
            mime_type=alter1(mime_type, self.mime_type),
            thumbnail=alter1(thumbnail, self.thumbnail),
        )


__all__ = ["Animation"]
