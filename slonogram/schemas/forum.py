from typing import Optional
from dataclasses import dataclass


@dataclass(slots=True)
class ForumTopicCreated:
    name: str
    icon_color: int
    icon_custom_emoji_id: Optional[str] = None


@dataclass(slots=True)
class ForumTopicClosed:
    pass


@dataclass(slots=True)
class ForumTopicReopened:
    pass


@dataclass(slots=True)
class ForumTopicEdited:
    name: Optional[str] = None
    icon_custom_emoji_id: Optional[str] = None


@dataclass(slots=True)
class GeneralForumTopicHidden:
    pass


@dataclass(slots=True)
class GeneralForumTopicUnhidden:
    pass


__all__ = [
    "GeneralForumTopicUnhidden",
    "ForumTopicEdited",
    "ForumTopicReopened",
    "ForumTopicClosed",
    "ForumTopicCreated",
]
