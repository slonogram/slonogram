from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass(slots=True)
class Voice:
    file_id: str
    file_unique_id: str

    duration: int
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@dataclass(slots=True)
class VideoNote:
    file_id: str
    file_unique_id: str

    length: int
    duration: int

    thumbnail: Optional[PhotoSize] = None
    file_size: Optional[int] = None


@dataclass(slots=True)
class Document:
    file_id: str
    file_unique_id: str
    thumbnail: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@dataclass(slots=True)
class Audio:
    file_id: str
    file_unique_id: str

    duration: int
    performer: Optional[str] = None
    title: Optional[str] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None
    thumbnail: Optional[PhotoSize] = None


@dataclass(slots=True)
class Animation:
    file_id: str
    file_unique_id: str

    width: int
    height: int

    duration: int
    thumbnail: PhotoSize
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@dataclass(slots=True)
class PhotoSize:
    file_id: str
    file_unique_id: str

    width: int
    height: int

    file_size: Optional[int] = None


__all__ = [
    "PhotoSize",
    "Animation",
    "Audio",
    "Document",
    "VideoNote",
    "Voice",
]
