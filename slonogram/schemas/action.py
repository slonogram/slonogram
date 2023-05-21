from typing import Optional, List
from .user import User
from dataclasses import dataclass


@dataclass
class ProximityAlertTriggered:
    traveler: User
    watcher: User
    distance: int


@dataclass
class VideoChatParticipantsInvited:
    users: List[User]


@dataclass
class VideoChatStarted:
    pass


@dataclass
class VideoChatEnded:
    duration: int


@dataclass
class VideoChatScheduled:
    start_date: int


@dataclass
class WriteAccessAllowed:
    web_app_name: Optional[str] = None


@dataclass
class MessageAutoDeleteTimerChanged:
    message_auto_delete_timer: int
