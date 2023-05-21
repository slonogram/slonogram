from __future__ import annotations

from .user import User
from .file import PhotoSize
from .passport import PassportData
from .shares import UserShared, ChatShared
from .payments import Invoice, SuccessfulPayment
from .forum import (
    ForumTopicCreated,
    ForumTopicEdited,
    ForumTopicClosed,
    ForumTopicReopened,
    GeneralForumTopicHidden,
    GeneralForumTopicUnhidden,
)
from .markup import InlineKeyboardMarkup
from .action import (
    MessageAutoDeleteTimerChanged,
    WriteAccessAllowed,
    ProximityAlertTriggered,
    VideoChatScheduled,
    VideoChatStarted,
    VideoChatEnded,
    VideoChatParticipantsInvited,
)
from .message_entity import MessageEntity

from typing import Optional, List, NewType
from dataclasses import dataclass
from enum import Enum

MessageId = NewType("MessageId", int)


class ParseMode(str, Enum):
    html = "HTML"
    markdown_v2 = "MarkdownV2"
    markdown = "Markdown"


@dataclass(slots=True)
class Message:
    id: int
    date: int
    chat: Chat

    message_thread_id: Optional[int] = None
    edit_date: Optional[int] = None

    from_: Optional[User] = None
    sender_chat: Optional[Chat] = None
    text: Optional[str] = None

    forward_from: Optional[User] = None
    forward_from_chat: Optional[Chat] = None
    forward_from_message_id: Optional[int] = None
    forward_signature: Optional[str] = None
    forward_sender_name: Optional[str] = None
    forward_date: Optional[int] = None
    author_signature: Optional[str] = None

    media_group_id: Optional[str] = None
    via_bot: Optional[User] = None

    entities: Optional[List[MessageEntity]] = None
    reply_to_message: Optional[Message] = None

    location: Optional[Location] = None
    left_chat_member: Optional[User] = None

    new_chat_title: Optional[str] = None
    new_chat_photo: Optional[List[PhotoSize]] = None
    message_auto_delete_timer_changed: Optional[
        MessageAutoDeleteTimerChanged
    ] = None

    migrate_to_chat_id: Optional[int] = None
    migrate_from_chat_id: Optional[int] = None

    pinned_message: Optional[Message] = None
    invoice: Optional[Invoice] = None
    successful_payment: Optional[SuccessfulPayment] = None

    user_shared: Optional[UserShared] = None
    chat_shared: Optional[ChatShared] = None

    connected_website: Optional[str] = None
    write_access_allowed: Optional[WriteAccessAllowed] = None

    passport_data: Optional[PassportData] = None
    proximity_alert_triggered: Optional[ProximityAlertTriggered] = None

    forum_topic_created: Optional[ForumTopicCreated] = None
    forum_topic_edited: Optional[ForumTopicEdited] = None
    forum_topic_closed: Optional[ForumTopicClosed] = None
    forum_topic_reopened: Optional[ForumTopicReopened] = None
    general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = None
    general_forum_topic_unhidden: Optional[
        GeneralForumTopicUnhidden
    ] = None

    video_chat_scheduled: Optional[VideoChatScheduled] = None
    video_chat_started: Optional[VideoChatStarted] = None
    video_chat_ended: Optional[VideoChatEnded] = None
    video_chat_participants_invited: Optional[
        VideoChatParticipantsInvited
    ] = None

    reply_markup: Optional[InlineKeyboardMarkup] = None

    channel_chat_created: bool = False
    supergroup_chat_created: bool = False
    group_chat_created: bool = False
    delete_chat_photo: bool = False
    is_topic_message: bool = False
    has_protected_content: bool = False
    is_automatic_forward: bool = False


@dataclass(slots=True)
class Location:
    longitude: float
    latitude: float

    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None


@dataclass(slots=True)
class ChatLocation:
    location: Location
    address: str


@dataclass(slots=True)
class ChatPermissions:
    can_send_messages: Optional[bool] = None
    can_send_audios: Optional[bool] = None
    can_send_documents: Optional[bool] = None
    can_send_photos: Optional[bool] = None
    can_send_videos: Optional[bool] = None
    can_send_video_notes: Optional[bool] = None
    can_send_voice_notes: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_manage_topics: Optional[bool] = None


class ChatType(str, Enum):
    private = "private"
    group = "group"
    supergroup = "supergroup"
    channel = "channel"


@dataclass(slots=True)
class Chat:
    id: int

    type_: ChatType

    title: Optional[str] = None
    username: Optional[str] = None

    first_name: Optional[str] = None
    last_name: Optional[str] = None

    active_usernames: Optional[List[str]] = None
    emoji_status_custom_emoji_id: Optional[str] = None
    bio: Optional[str] = None
    description: Optional[str] = None

    invite_link: Optional[str] = None
    pinned_message: Optional[Message] = None
    permissions: Optional[ChatPermissions] = None

    slow_mode_delay: Optional[int] = None
    message_auto_delete_timer: Optional[int] = None

    sticker_set_name: Optional[str] = None

    linked_chat_id: Optional[int] = None

    can_set_sticker_set: bool = False
    has_hidden_members: bool = False
    has_protected_content: bool = False
    has_aggressive_anti_spam_enabled: bool = False
    has_private_forwards: bool = False
    has_restricted_voice_and_video_messages: bool = False
    join_to_send_messages: bool = False
    join_by_request: bool = False
    is_forum: bool = False


__all__ = [
    "Chat",
    "ChatType",
    "ChatPermissions",
    "ChatLocation",
    "Location",
    "Message",
    "ParseMode",
]
