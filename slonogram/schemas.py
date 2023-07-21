# flake8: noqa
from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, IO, TypeAlias


class ChatAction(str, Enum):
    TYPING = "typing"
    UPLOAD_PHOTO = "upload_photo"
    RECORD_VIDEO = "record_video"
    UPLOAD_VIDEO = "upload_video"
    RECORD_VOICE = "record_voice"
    UPLOAD_VOICE = "upload_voice"
    UPLOAD_DOCUMENT = "upload_document"
    CHOOSE_STICKER = "choose_sticker"
    FIND_LOCATION = "find_location"
    RECORD_VIDEO_NOTE = "record_video_note"
    UPLOAD_VIDEO_NOTE = "upload_video_note"


class EntityType(str, Enum):
    MENTION = "mention"
    HASHTAG = "hashtag"
    CASHTAG = "cashtag"
    BOT_COMMAND = "bot_command"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    SPOILER = "spoiler"
    CODE = "code"
    PRE = "pre"
    TEXT_LINK = "text_link"
    TEXT_MENTION = "text_mention"
    CUSTOM_EMOJI = "custom_emoji"


class UpdateType(str, Enum):
    MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    CHANNEL_POST = "channel_post"
    EDITED_CHANNEL_POST = "edited_channel_post"
    INLINE_QUERY = "inline_query"
    CHOSEN_INLINE_RESULT = "chosen_inline_result"
    CALLBACK_QUERY = "callback_query"
    SHIPPING_QUERY = "shipping_query"
    PRE_CHECKOUT_QUERY = "pre_checkout_query"
    POLL = "poll"
    POLL_ANSWER = "poll_answer"
    MY_CHAT_MEMBER = "my_chat_member"
    CHAT_MEMBER = "chat_member"
    CHAT_JOIN_REQUEST = "chat_join_request"


class ParseMode(str, Enum):
    MARKDOWN_V2 = "MarkdownV2"
    HTML = "HTML"
    MARKDOWN = "Markdown"


@dataclass(slots=True)
class Update:
    id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
    inline_query: Optional[InlineQuery] = None
    chosen_inline_result: Optional[ChosenInlineResult] = None
    callback_query: Optional[CallbackQuery] = None
    shipping_query: Optional[ShippingQuery] = None
    pre_checkout_query: Optional[PreCheckoutQuery] = None
    poll: Optional[Poll] = None
    poll_answer: Optional[PollAnswer] = None
    my_chat_member: Optional[ChatMemberUpdated] = None
    chat_member: Optional[ChatMemberUpdated] = None
    chat_join_request: Optional[ChatJoinRequest] = None


@dataclass(slots=True)
class WebhookInfo:
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: Optional[str] = None
    last_error_date: Optional[int] = None
    last_error_message: Optional[str] = None
    last_synchronization_error_date: Optional[int] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[str]] = None


@dataclass(slots=True)
class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    is_premium: Optional[bool] = None
    added_to_attachment_menu: Optional[bool] = None
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None


@dataclass(slots=True)
class Chat:
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_forum: Optional[bool] = None
    photo: Optional[ChatPhoto] = None
    active_usernames: Optional[List[str]] = None
    emoji_status_custom_emoji_id: Optional[str] = None
    bio: Optional[str] = None
    has_private_forwards: Optional[bool] = None
    has_restricted_voice_and_video_messages: Optional[bool] = None
    join_to_send_messages: Optional[bool] = None
    join_by_request: Optional[bool] = None
    description: Optional[str] = None
    invite_link: Optional[str] = None
    pinned_message: Optional[Message] = None
    permissions: Optional[ChatPermissions] = None
    slow_mode_delay: Optional[int] = None
    message_auto_delete_time: Optional[int] = None
    has_aggressive_anti_spam_enabled: Optional[bool] = None
    has_hidden_members: Optional[bool] = None
    has_protected_content: Optional[bool] = None
    sticker_set_name: Optional[str] = None
    can_set_sticker_set: Optional[bool] = None
    linked_chat_id: Optional[int] = None
    location: Optional[ChatLocation] = None


@dataclass(slots=True)
class Message:
    id: int
    date: int
    chat: Chat
    message_thread_id: Optional[int] = None
    from_: Optional[User] = None
    sender_chat: Optional[Chat] = None
    forward_from: Optional[User] = None
    forward_from_chat: Optional[Chat] = None
    forward_from_message_id: Optional[int] = None
    forward_signature: Optional[str] = None
    forward_sender_name: Optional[str] = None
    forward_date: Optional[int] = None
    is_topic_message: Optional[bool] = None
    is_automatic_forward: Optional[bool] = None
    reply_to_message: Optional[Message] = None
    via_bot: Optional[User] = None
    edit_date: Optional[int] = None
    has_protected_content: Optional[bool] = None
    media_group_id: Optional[str] = None
    author_signature: Optional[str] = None
    text: Optional[str] = None
    entities: Optional[List[MessageEntity]] = None
    animation: Optional[Animation] = None
    audio: Optional[Audio] = None
    document: Optional[Document] = None
    photo: Optional[List[PhotoSize]] = None
    sticker: Optional[Sticker] = None
    video: Optional[Video] = None
    video_note: Optional[VideoNote] = None
    voice: Optional[Voice] = None
    caption: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    has_media_spoiler: Optional[bool] = None
    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    poll: Optional[Poll] = None
    venue: Optional[Venue] = None
    location: Optional[Location] = None
    new_chat_members: Optional[List[User]] = None
    left_chat_member: Optional[User] = None
    new_chat_title: Optional[str] = None
    new_chat_photo: Optional[List[PhotoSize]] = None
    delete_chat_photo: Optional[bool] = None
    group_chat_created: Optional[bool] = None
    supergroup_chat_created: Optional[bool] = None
    channel_chat_created: Optional[bool] = None
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
    web_app_data: Optional[WebAppData] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass(slots=True)
class MessageId:
    message_id: int


@dataclass(slots=True)
class MessageEntity:
    type: EntityType
    offset: int
    length: int
    url: Optional[str] = None
    user: Optional[User] = None
    language: Optional[str] = None
    custom_emoji_id: Optional[str] = None


@dataclass(slots=True)
class PhotoSize:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int] = None


@dataclass(slots=True)
class Animation:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
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
class Document:
    file_id: str
    file_unique_id: str
    thumbnail: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@dataclass(slots=True)
class Video:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: Optional[PhotoSize] = None
    file_name: Optional[str] = None
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
class Voice:
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@dataclass(slots=True)
class Contact:
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    user_id: Optional[int] = None
    vcard: Optional[str] = None


@dataclass(slots=True)
class Dice:
    emoji: str
    value: int


@dataclass(slots=True)
class PollOption:
    text: str
    voter_count: int


@dataclass(slots=True)
class PollAnswer:
    poll_id: str
    user: User
    option_ids: List[int]


@dataclass(slots=True)
class Poll:
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None
    explanation_entities: Optional[List[MessageEntity]] = None
    open_period: Optional[int] = None
    close_date: Optional[int] = None


@dataclass(slots=True)
class Location:
    longitude: float
    latitude: float
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None


@dataclass(slots=True)
class Venue:
    location: Location
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None


@dataclass(slots=True)
class WebAppData:
    data: str
    button_text: str


@dataclass(slots=True)
class ProximityAlertTriggered:
    traveler: User
    watcher: User
    distance: int


@dataclass(slots=True)
class MessageAutoDeleteTimerChanged:
    message_auto_delete_time: int


@dataclass(slots=True)
class ForumTopicCreated:
    name: str
    icon_color: int
    icon_custom_emoji_id: Optional[str] = None


@dataclass(slots=True)
class ForumTopicClosed:
    pass


@dataclass(slots=True)
class ForumTopicEdited:
    name: Optional[str] = None
    icon_custom_emoji_id: Optional[str] = None


@dataclass(slots=True)
class ForumTopicReopened:
    pass


@dataclass(slots=True)
class GeneralForumTopicHidden:
    pass


@dataclass(slots=True)
class GeneralForumTopicUnhidden:
    pass


@dataclass(slots=True)
class UserShared:
    request_id: int
    user_id: int


@dataclass(slots=True)
class ChatShared:
    request_id: int
    chat_id: int


@dataclass(slots=True)
class WriteAccessAllowed:
    web_app_name: Optional[str] = None


@dataclass(slots=True)
class VideoChatScheduled:
    start_date: int


@dataclass(slots=True)
class VideoChatStarted:
    pass


@dataclass(slots=True)
class VideoChatEnded:
    duration: int


@dataclass(slots=True)
class VideoChatParticipantsInvited:
    users: List[User]


@dataclass(slots=True)
class UserProfilePhotos:
    total_count: int
    photos: List[List[PhotoSize]]


@dataclass(slots=True)
class File:
    file_id: str
    file_unique_id: str
    file_size: Optional[int] = None
    file_path: Optional[str] = None


@dataclass(slots=True)
class WebAppInfo:
    url: str


@dataclass(slots=True)
class ReplyKeyboardMarkup:
    keyboard: List[List[KeyboardButton]]
    is_persistent: Optional[bool] = None
    resize_keyboard: Optional[bool] = None
    one_time_keyboard: Optional[bool] = None
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None


@dataclass(slots=True)
class KeyboardButton:
    text: str
    request_user: Optional[KeyboardButtonRequestUser] = None
    request_chat: Optional[KeyboardButtonRequestChat] = None
    request_contact: Optional[bool] = None
    request_location: Optional[bool] = None
    request_poll: Optional[KeyboardButtonPollType] = None
    web_app: Optional[WebAppInfo] = None


@dataclass(slots=True)
class KeyboardButtonRequestUser:
    request_id: int
    user_is_bot: Optional[bool] = None
    user_is_premium: Optional[bool] = None


@dataclass(slots=True)
class KeyboardButtonRequestChat:
    request_id: int
    chat_is_channel: bool
    chat_is_forum: Optional[bool] = None
    chat_has_username: Optional[bool] = None
    chat_is_created: Optional[bool] = None
    user_administrator_rights: Optional[ChatAdministratorRights] = None
    bot_administrator_rights: Optional[ChatAdministratorRights] = None
    bot_is_member: Optional[bool] = None


@dataclass(slots=True)
class KeyboardButtonPollType:
    type: Optional[str] = None


@dataclass(slots=True)
class ReplyKeyboardRemove:
    remove_keyboard: bool
    selective: Optional[bool] = None


@dataclass(slots=True)
class InlineKeyboardMarkup:
    inline_keyboard: List[List[InlineKeyboardButton]]


@dataclass(slots=True)
class InlineKeyboardButton:
    text: str
    url: Optional[str] = None
    callback_data: Optional[str] = None
    web_app: Optional[WebAppInfo] = None
    login_url: Optional[LoginUrl] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    switch_inline_query_chosen_chat: Optional[
        SwitchInlineQueryChosenChat
    ] = None
    callback_game: Optional[CallbackGame] = None
    pay: Optional[bool] = None


@dataclass(slots=True)
class LoginUrl:
    url: str
    forward_text: Optional[str] = None
    bot_username: Optional[str] = None
    request_write_access: Optional[bool] = None


@dataclass(slots=True)
class SwitchInlineQueryChosenChat:
    query: Optional[str] = None
    allow_user_chats: Optional[bool] = None
    allow_bot_chats: Optional[bool] = None
    allow_group_chats: Optional[bool] = None
    allow_channel_chats: Optional[bool] = None


@dataclass(slots=True)
class CallbackQuery:
    id: str
    from_: User
    chat_instance: str
    message: Optional[Message] = None
    inline_message_id: Optional[str] = None
    data: Optional[str] = None
    game_short_name: Optional[str] = None


@dataclass(slots=True)
class ForceReply:
    force_reply: bool
    input_field_placeholder: Optional[str] = None
    selective: Optional[bool] = None


@dataclass(slots=True)
class ChatPhoto:
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


@dataclass(slots=True)
class ChatInviteLink:
    invite_link: str
    creator: User
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: Optional[str] = None
    expire_date: Optional[int] = None
    member_limit: Optional[int] = None
    pending_join_request_count: Optional[int] = None


@dataclass(slots=True)
class ChatAdministratorRights:
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_manage_topics: Optional[bool] = None


@dataclass(slots=True)
class ChatMember:
    pass


@dataclass(slots=True)
class ChatMemberOwner:
    status: str
    user: User
    is_anonymous: bool
    custom_title: Optional[str] = None


@dataclass(slots=True)
class ChatMemberAdministrator:
    status: str
    user: User
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_manage_topics: Optional[bool] = None
    custom_title: Optional[str] = None


@dataclass(slots=True)
class ChatMemberMember:
    status: str
    user: User


@dataclass(slots=True)
class ChatMemberRestricted:
    status: str
    user: User
    is_member: bool
    can_send_messages: bool
    can_send_audios: bool
    can_send_documents: bool
    can_send_photos: bool
    can_send_videos: bool
    can_send_video_notes: bool
    can_send_voice_notes: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool
    until_date: int


@dataclass(slots=True)
class ChatMemberLeft:
    status: str
    user: User


@dataclass(slots=True)
class ChatMemberBanned:
    status: str
    user: User
    until_date: int


@dataclass(slots=True)
class ChatMemberUpdated:
    chat: Chat
    from_: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: Optional[ChatInviteLink] = None
    via_chat_folder_invite_link: Optional[bool] = None


@dataclass(slots=True)
class ChatJoinRequest:
    chat: Chat
    from_: User
    user_chat_id: int
    date: int
    bio: Optional[str] = None
    invite_link: Optional[ChatInviteLink] = None


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


@dataclass(slots=True)
class ChatLocation:
    location: Location
    address: str


@dataclass(slots=True)
class ForumTopic:
    message_thread_id: int
    name: str
    icon_color: int
    icon_custom_emoji_id: Optional[str] = None


@dataclass(slots=True)
class BotCommand:
    command: str
    description: str


@dataclass(slots=True)
class BotCommandScope:
    pass


@dataclass(slots=True)
class BotCommandScopeDefault:
    type: str


@dataclass(slots=True)
class BotCommandScopeAllPrivateChats:
    type: str


@dataclass(slots=True)
class BotCommandScopeAllGroupChats:
    type: str


@dataclass(slots=True)
class BotCommandScopeAllChatAdministrators:
    type: str


@dataclass(slots=True)
class BotCommandScopeChat:
    type: str
    chat_id: int | str


@dataclass(slots=True)
class BotCommandScopeChatAdministrators:
    type: str
    chat_id: int | str


@dataclass(slots=True)
class BotCommandScopeChatMember:
    type: str
    chat_id: int | str
    user_id: int


@dataclass(slots=True)
class BotName:
    name: str


@dataclass(slots=True)
class BotDescription:
    description: str


@dataclass(slots=True)
class BotShortDescription:
    short_description: str


@dataclass(slots=True)
class MenuButton:
    pass


@dataclass(slots=True)
class MenuButtonCommands:
    type: str


@dataclass(slots=True)
class MenuButtonWebApp:
    type: str
    text: str
    web_app: WebAppInfo


@dataclass(slots=True)
class MenuButtonDefault:
    type: str


@dataclass(slots=True)
class ResponseParameters:
    migrate_to_chat_id: Optional[int] = None
    retry_after: Optional[int] = None


@dataclass(slots=True)
class InputMediaPhoto:
    type: str
    media: str
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    has_spoiler: Optional[bool] = None


@dataclass(slots=True)
class InputMediaVideo:
    type: str
    media: str
    thumbnail: Optional[IO[bytes] | str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    supports_streaming: Optional[bool] = None
    has_spoiler: Optional[bool] = None


@dataclass(slots=True)
class InputMediaAnimation:
    type: str
    media: str
    thumbnail: Optional[IO[bytes] | str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None
    has_spoiler: Optional[bool] = None


@dataclass(slots=True)
class InputMediaAudio:
    type: str
    media: str
    thumbnail: Optional[IO[bytes] | str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    duration: Optional[int] = None
    performer: Optional[str] = None
    title: Optional[str] = None


@dataclass(slots=True)
class InputMediaDocument:
    type: str
    media: str
    thumbnail: Optional[IO[bytes] | str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    disable_content_type_detection: Optional[bool] = None


@dataclass(slots=True)
class InputFile:
    pass


@dataclass(slots=True)
class Sticker:
    file_id: str
    file_unique_id: str
    type: str
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumbnail: Optional[PhotoSize] = None
    emoji: Optional[str] = None
    set_name: Optional[str] = None
    premium_animation: Optional[File] = None
    mask_position: Optional[MaskPosition] = None
    custom_emoji_id: Optional[str] = None
    needs_repainting: Optional[bool] = None
    file_size: Optional[int] = None


@dataclass(slots=True)
class StickerSet:
    name: str
    title: str
    sticker_type: str
    is_animated: bool
    is_video: bool
    stickers: List[Sticker]
    thumbnail: Optional[PhotoSize] = None


@dataclass(slots=True)
class MaskPosition:
    point: str
    x_shift: float
    y_shift: float
    scale: float


@dataclass(slots=True)
class InputSticker:
    sticker: IO[bytes] | str
    emoji_list: List[str]
    mask_position: Optional[MaskPosition] = None
    keywords: Optional[List[str]] = None


@dataclass(slots=True)
class InlineQuery:
    id: str
    from_: User
    query: str
    offset: str
    chat_type: Optional[str] = None
    location: Optional[Location] = None


@dataclass(slots=True)
class InlineQueryResultsButton:
    text: str
    web_app: Optional[WebAppInfo] = None
    start_parameter: Optional[str] = None


@dataclass(slots=True)
class InlineQueryResultArticle:
    type: str
    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: Optional[InlineKeyboardMarkup] = None
    url: Optional[str] = None
    hide_url: Optional[bool] = None
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


@dataclass(slots=True)
class InlineQueryResultPhoto:
    type: str
    id: str
    photo_url: str
    thumbnail_url: str
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultGif:
    type: str
    id: str
    gif_url: str
    thumbnail_url: str
    gif_width: Optional[int] = None
    gif_height: Optional[int] = None
    gif_duration: Optional[int] = None
    thumbnail_mime_type: Optional[str] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultMpeg4Gif:
    type: str
    id: str
    mpeg4_url: str
    thumbnail_url: str
    mpeg4_width: Optional[int] = None
    mpeg4_height: Optional[int] = None
    mpeg4_duration: Optional[int] = None
    thumbnail_mime_type: Optional[str] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultVideo:
    type: str
    id: str
    video_url: str
    mime_type: str
    thumbnail_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    video_width: Optional[int] = None
    video_height: Optional[int] = None
    video_duration: Optional[int] = None
    description: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultAudio:
    type: str
    id: str
    audio_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    performer: Optional[str] = None
    audio_duration: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultVoice:
    type: str
    id: str
    voice_url: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    voice_duration: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultDocument:
    type: str
    id: str
    title: str
    document_url: str
    mime_type: str
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    description: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


@dataclass(slots=True)
class InlineQueryResultLocation:
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


@dataclass(slots=True)
class InlineQueryResultVenue:
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


@dataclass(slots=True)
class InlineQueryResultContact:
    type: str
    id: str
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None
    thumbnail_url: Optional[str] = None
    thumbnail_width: Optional[int] = None
    thumbnail_height: Optional[int] = None


@dataclass(slots=True)
class InlineQueryResultGame:
    type: str
    id: str
    game_short_name: str
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass(slots=True)
class InlineQueryResultCachedPhoto:
    type: str
    id: str
    photo_file_id: str
    title: Optional[str] = None
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultCachedGif:
    type: str
    id: str
    gif_file_id: str
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultCachedMpeg4Gif:
    type: str
    id: str
    mpeg4_file_id: str
    title: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultCachedSticker:
    type: str
    id: str
    sticker_file_id: str
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultCachedDocument:
    type: str
    id: str
    title: str
    document_file_id: str
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultCachedVideo:
    type: str
    id: str
    video_file_id: str
    title: str
    description: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultCachedVoice:
    type: str
    id: str
    voice_file_id: str
    title: str
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InlineQueryResultCachedAudio:
    type: str
    id: str
    audio_file_id: str
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None
    input_message_content: Optional[InputMessageContent] = None


@dataclass(slots=True)
class InputTextMessageContent:
    message_text: str
    parse_mode: Optional[str] = None
    entities: Optional[List[MessageEntity]] = None
    disable_web_page_preview: Optional[bool] = None


@dataclass(slots=True)
class InputLocationMessageContent:
    latitude: float
    longitude: float
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None


@dataclass(slots=True)
class InputVenueMessageContent:
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None


@dataclass(slots=True)
class InputContactMessageContent:
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None


@dataclass(slots=True)
class InputInvoiceMessageContent:
    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: List[LabeledPrice]
    max_tip_amount: Optional[int] = None
    suggested_tip_amounts: Optional[List[int]] = None
    provider_data: Optional[str] = None
    photo_url: Optional[str] = None
    photo_size: Optional[int] = None
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    need_name: Optional[bool] = None
    need_phone_number: Optional[bool] = None
    need_email: Optional[bool] = None
    need_shipping_address: Optional[bool] = None
    send_phone_number_to_provider: Optional[bool] = None
    send_email_to_provider: Optional[bool] = None
    is_flexible: Optional[bool] = None


@dataclass(slots=True)
class ChosenInlineResult:
    result_id: str
    from_: User
    query: str
    location: Optional[Location] = None
    inline_message_id: Optional[str] = None


@dataclass(slots=True)
class SentWebAppMessage:
    inline_message_id: Optional[str] = None


@dataclass(slots=True)
class LabeledPrice:
    label: str
    amount: int


@dataclass(slots=True)
class Invoice:
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


@dataclass(slots=True)
class ShippingAddress:
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


@dataclass(slots=True)
class OrderInfo:
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    shipping_address: Optional[ShippingAddress] = None


@dataclass(slots=True)
class ShippingOption:
    id: str
    title: str
    prices: List[LabeledPrice]


@dataclass(slots=True)
class SuccessfulPayment:
    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None


@dataclass(slots=True)
class ShippingQuery:
    id: str
    from_: User
    invoice_payload: str
    shipping_address: ShippingAddress


@dataclass(slots=True)
class PreCheckoutQuery:
    id: str
    from_: User
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None


@dataclass(slots=True)
class PassportData:
    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials


@dataclass(slots=True)
class PassportFile:
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


@dataclass(slots=True)
class EncryptedPassportElement:
    type: str
    hash: str
    data: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    files: Optional[List[PassportFile]] = None
    front_side: Optional[PassportFile] = None
    reverse_side: Optional[PassportFile] = None
    selfie: Optional[PassportFile] = None
    translation: Optional[List[PassportFile]] = None


@dataclass(slots=True)
class EncryptedCredentials:
    data: str
    hash: str
    secret: str


@dataclass(slots=True)
class PassportElementError:
    pass


@dataclass(slots=True)
class PassportElementErrorDataField:
    source: str
    type: str
    field_name: str
    data_hash: str
    message: str


@dataclass(slots=True)
class PassportElementErrorFrontSide:
    source: str
    type: str
    file_hash: str
    message: str


@dataclass(slots=True)
class PassportElementErrorReverseSide:
    source: str
    type: str
    file_hash: str
    message: str


@dataclass(slots=True)
class PassportElementErrorSelfie:
    source: str
    type: str
    file_hash: str
    message: str


@dataclass(slots=True)
class PassportElementErrorFile:
    source: str
    type: str
    file_hash: str
    message: str


@dataclass(slots=True)
class PassportElementErrorFiles:
    source: str
    type: str
    file_hashes: List[str]
    message: str


@dataclass(slots=True)
class PassportElementErrorTranslationFile:
    source: str
    type: str
    file_hash: str
    message: str


@dataclass(slots=True)
class PassportElementErrorTranslationFiles:
    source: str
    type: str
    file_hashes: List[str]
    message: str


@dataclass(slots=True)
class PassportElementErrorUnspecified:
    source: str
    type: str
    element_hash: str
    message: str


@dataclass(slots=True)
class Game:
    title: str
    description: str
    photo: List[PhotoSize]
    text: Optional[str] = None
    text_entities: Optional[List[MessageEntity]] = None
    animation: Optional[Animation] = None


@dataclass(slots=True)
class CallbackGame:
    pass


@dataclass(slots=True)
class GameHighScore:
    position: int
    user: User
    score: int


InputMedia: TypeAlias = (
    InputMediaAnimation
    | InputMediaDocument
    | InputMediaAudio
    | InputMediaPhoto
    | InputMediaVideo
)
InlineQueryResult: TypeAlias = (
    InlineQueryResultCachedAudio
    | InlineQueryResultCachedDocument
    | InlineQueryResultCachedGif
    | InlineQueryResultCachedMpeg4Gif
    | InlineQueryResultCachedPhoto
    | InlineQueryResultCachedSticker
    | InlineQueryResultCachedVideo
    | InlineQueryResultCachedVoice
    | InlineQueryResultArticle
    | InlineQueryResultAudio
    | InlineQueryResultContact
    | InlineQueryResultGame
    | InlineQueryResultDocument
    | InlineQueryResultGif
    | InlineQueryResultLocation
    | InlineQueryResultMpeg4Gif
    | InlineQueryResultPhoto
    | InlineQueryResultVenue
    | InlineQueryResultVideo
    | InlineQueryResultVoice
)
InputMessageContent: TypeAlias = (
    InputTextMessageContent
    | InputLocationMessageContent
    | InputVenueMessageContent
    | InputContactMessageContent
    | InputInvoiceMessageContent
)
