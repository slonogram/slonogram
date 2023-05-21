from typing import Optional
from dataclasses import dataclass


@dataclass
class ForumTopicCreated:
    name: str
    icon_color: int
    icon_custom_emoji_id: Optional[str] = None


@dataclass
class ForumTopicClosed:
    pass


@dataclass
class ForumTopicReopened:
    pass


@dataclass
class ForumTopicEdited:
    name: Optional[str] = None
    icon_custom_emoji_id: Optional[str] = None


@dataclass
class GeneralForumTopicHidden:
    pass


@dataclass
class GeneralForumTopicUnhidden:
    pass
