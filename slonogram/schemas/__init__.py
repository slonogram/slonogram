"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from slonogram.schemas.login_url import LoginUrl
from slonogram.schemas.chat_photo import ChatPhoto
from slonogram.schemas.message_entity import MessageEntity
from slonogram.schemas.audio import Audio
from slonogram.schemas.input_message_content import (
    InputContactMessageContent,
    InputInvoiceMessageContent,
    InputLocationMessageContent,
    InputMessageContent,
    InputTextMessageContent,
    InputVenueMessageContent,
)
from slonogram.schemas.forum_topic_created import ForumTopicCreated
from slonogram.schemas.reaction_count import ReactionCount
from slonogram.schemas.callback_query import CallbackQuery
from slonogram.schemas.poll import Poll
from slonogram.schemas.video_note import VideoNote
from slonogram.schemas.response_parameters import ResponseParameters
from slonogram.schemas.inline_keyboard_markup import InlineKeyboardMarkup
from slonogram.schemas.forum_topic_edited import ForumTopicEdited
from slonogram.schemas.bot_command import BotCommand
from slonogram.schemas.chat_shared import ChatShared
from slonogram.schemas.web_app_data import WebAppData
from slonogram.schemas.update import Update
from slonogram.schemas.user_profile_photos import UserProfilePhotos
from slonogram.schemas.sticker_set import StickerSet
from slonogram.schemas.message_reaction_updated import MessageReactionUpdated
from slonogram.schemas.document import Document
from slonogram.schemas.successful_payment import SuccessfulPayment
from slonogram.schemas.inline_query_results_button import InlineQueryResultsButton
from slonogram.schemas.forum_topic_reopened import ForumTopicReopened
from slonogram.schemas.sent_web_app_message import SentWebAppMessage
from slonogram.schemas.labeled_price import LabeledPrice
from slonogram.schemas.video import Video
from slonogram.schemas.video_chat_scheduled import VideoChatScheduled
from slonogram.schemas.mask_position import MaskPosition
from slonogram.schemas.venue import Venue
from slonogram.schemas.encrypted_passport_element import EncryptedPassportElement
from slonogram.schemas.input_file import InputFile
from slonogram.schemas.write_access_allowed import WriteAccessAllowed
from slonogram.schemas.passport_element_error import (
    PassportElementError,
    PassportElementErrorDataField,
    PassportElementErrorFile,
    PassportElementErrorFiles,
    PassportElementErrorFrontSide,
    PassportElementErrorReverseSide,
    PassportElementErrorSelfie,
    PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified,
)
from slonogram.schemas.external_reply_info import ExternalReplyInfo
from slonogram.schemas.general_forum_topic_unhidden import GeneralForumTopicUnhidden
from slonogram.schemas.bot_description import BotDescription
from slonogram.schemas.order_info import OrderInfo
from slonogram.schemas.pre_checkout_query import PreCheckoutQuery
from slonogram.schemas.inline_query import InlineQuery
from slonogram.schemas.maybe_inaccessible_message import (
    InaccessibleMessage,
    MaybeInaccessibleMessage,
    Message,
)
from slonogram.schemas.input_media import (
    InputMedia,
    InputMediaAnimation,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
)
from slonogram.schemas.chosen_inline_result import ChosenInlineResult
from slonogram.schemas.bot_name import BotName
from slonogram.schemas.story import Story
from slonogram.schemas.chat_boost import ChatBoost
from slonogram.schemas.message_origin import (
    MessageOrigin,
    MessageOriginChannel,
    MessageOriginChat,
    MessageOriginHiddenUser,
    MessageOriginUser,
)
from slonogram.schemas.menu_button import (
    MenuButton,
    MenuButtonCommands,
    MenuButtonDefault,
    MenuButtonWebApp,
)
from slonogram.schemas.sticker import Sticker
from slonogram.schemas.webhook_info import WebhookInfo
from slonogram.schemas.animation import Animation
from slonogram.schemas.user_chat_boosts import UserChatBoosts
from slonogram.schemas.chat_boost_added import ChatBoostAdded
from slonogram.schemas.message_id import MessageId
from slonogram.schemas.chat_permissions import ChatPermissions
from slonogram.schemas.giveaway import Giveaway
from slonogram.schemas.giveaway_completed import GiveawayCompleted
from slonogram.schemas.chat_boost_updated import ChatBoostUpdated
from slonogram.schemas.chat_administrator_rights import ChatAdministratorRights
from slonogram.schemas.input_sticker import InputSticker
from slonogram.schemas.link_preview_options import LinkPreviewOptions
from slonogram.schemas.contact import Contact
from slonogram.schemas.chat_member_updated import ChatMemberUpdated
from slonogram.schemas.video_chat_started import VideoChatStarted
from slonogram.schemas.shipping_query import ShippingQuery
from slonogram.schemas.photo_size import PhotoSize
from slonogram.schemas.location import Location
from slonogram.schemas.game_high_score import GameHighScore
from slonogram.schemas.inline_keyboard_button import InlineKeyboardButton
from slonogram.schemas.callback_game import CallbackGame
from slonogram.schemas.message_reaction_count_updated import MessageReactionCountUpdated
from slonogram.schemas.chat_member import (
    ChatMember,
    ChatMemberAdministrator,
    ChatMemberBanned,
    ChatMemberLeft,
    ChatMemberMember,
    ChatMemberOwner,
    ChatMemberRestricted,
)
from slonogram.schemas.text_quote import TextQuote
from slonogram.schemas.chat_location import ChatLocation
from slonogram.schemas.general_forum_topic_hidden import GeneralForumTopicHidden
from slonogram.schemas.reply_keyboard_remove import ReplyKeyboardRemove
from slonogram.schemas.keyboard_button_request_chat import KeyboardButtonRequestChat
from slonogram.schemas.forum_topic import ForumTopic
from slonogram.schemas.inline_query_result import (
    InlineQueryResult,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InlineQueryResultContact,
    InlineQueryResultDocument,
    InlineQueryResultGame,
    InlineQueryResultGif,
    InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoice,
)
from slonogram.schemas.reply_parameters import ReplyParameters
from slonogram.schemas.poll_answer import PollAnswer
from slonogram.schemas.proximity_alert_triggered import ProximityAlertTriggered
from slonogram.schemas.chat_boost_source import (
    ChatBoostSource,
    ChatBoostSourceGiftCode,
    ChatBoostSourceGiveaway,
    ChatBoostSourcePremium,
)
from slonogram.schemas.message_auto_delete_timer_changed import (
    MessageAutoDeleteTimerChanged,
)
from slonogram.schemas.voice import Voice
from slonogram.schemas.video_chat_ended import VideoChatEnded
from slonogram.schemas.bot_command_scope import (
    BotCommandScope,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
    BotCommandScopeDefault,
)
from slonogram.schemas.user import User
from slonogram.schemas.poll_option import PollOption
from slonogram.schemas.web_app_info import WebAppInfo
from slonogram.schemas.video_chat_participants_invited import (
    VideoChatParticipantsInvited,
)
from slonogram.schemas.force_reply import ForceReply
from slonogram.schemas.chat_invite_link import ChatInviteLink
from slonogram.schemas.dice import Dice
from slonogram.schemas.encrypted_credentials import EncryptedCredentials
from slonogram.schemas.invoice import Invoice
from slonogram.schemas.passport_data import PassportData
from slonogram.schemas.bot_short_description import BotShortDescription
from slonogram.schemas.reply_keyboard_markup import ReplyKeyboardMarkup
from slonogram.schemas.chat_boost_removed import ChatBoostRemoved
from slonogram.schemas.game import Game
from slonogram.schemas.shipping_address import ShippingAddress
from slonogram.schemas.file import File
from slonogram.schemas.giveaway_created import GiveawayCreated
from slonogram.schemas.switch_inline_query_chosen_chat import (
    SwitchInlineQueryChosenChat,
)
from slonogram.schemas.shipping_option import ShippingOption
from slonogram.schemas.chat import Chat
from slonogram.schemas.keyboard_button_poll_type import KeyboardButtonPollType
from slonogram.schemas.giveaway_winners import GiveawayWinners
from slonogram.schemas.reaction_type import (
    ReactionType,
    ReactionTypeCustomEmoji,
    ReactionTypeEmoji,
)
from slonogram.schemas.users_shared import UsersShared
from slonogram.schemas.keyboard_button import KeyboardButton
from slonogram.schemas.keyboard_button_request_users import KeyboardButtonRequestUsers
from slonogram.schemas.passport_file import PassportFile
from slonogram.schemas.forum_topic_closed import ForumTopicClosed
from slonogram.schemas.chat_join_request import ChatJoinRequest

__all__ = [
    "LoginUrl",
    "ChatPhoto",
    "MessageEntity",
    "Audio",
    "InputContactMessageContent",
    "InputInvoiceMessageContent",
    "InputLocationMessageContent",
    "InputMessageContent",
    "InputTextMessageContent",
    "InputVenueMessageContent",
    "ForumTopicCreated",
    "ReactionCount",
    "CallbackQuery",
    "Poll",
    "VideoNote",
    "ResponseParameters",
    "InlineKeyboardMarkup",
    "ForumTopicEdited",
    "BotCommand",
    "ChatShared",
    "WebAppData",
    "Update",
    "UserProfilePhotos",
    "StickerSet",
    "MessageReactionUpdated",
    "Document",
    "SuccessfulPayment",
    "InlineQueryResultsButton",
    "ForumTopicReopened",
    "SentWebAppMessage",
    "LabeledPrice",
    "Video",
    "VideoChatScheduled",
    "MaskPosition",
    "Venue",
    "EncryptedPassportElement",
    "InputFile",
    "WriteAccessAllowed",
    "PassportElementError",
    "PassportElementErrorDataField",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "ExternalReplyInfo",
    "GeneralForumTopicUnhidden",
    "BotDescription",
    "OrderInfo",
    "PreCheckoutQuery",
    "InlineQuery",
    "InaccessibleMessage",
    "MaybeInaccessibleMessage",
    "Message",
    "InputMedia",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputMediaPhoto",
    "InputMediaVideo",
    "ChosenInlineResult",
    "BotName",
    "Story",
    "ChatBoost",
    "MessageOrigin",
    "MessageOriginChannel",
    "MessageOriginChat",
    "MessageOriginHiddenUser",
    "MessageOriginUser",
    "MenuButton",
    "MenuButtonCommands",
    "MenuButtonDefault",
    "MenuButtonWebApp",
    "Sticker",
    "WebhookInfo",
    "Animation",
    "UserChatBoosts",
    "ChatBoostAdded",
    "MessageId",
    "ChatPermissions",
    "Giveaway",
    "GiveawayCompleted",
    "ChatBoostUpdated",
    "ChatAdministratorRights",
    "InputSticker",
    "LinkPreviewOptions",
    "Contact",
    "ChatMemberUpdated",
    "VideoChatStarted",
    "ShippingQuery",
    "PhotoSize",
    "Location",
    "GameHighScore",
    "InlineKeyboardButton",
    "CallbackGame",
    "MessageReactionCountUpdated",
    "ChatMember",
    "ChatMemberAdministrator",
    "ChatMemberBanned",
    "ChatMemberLeft",
    "ChatMemberMember",
    "ChatMemberOwner",
    "ChatMemberRestricted",
    "TextQuote",
    "ChatLocation",
    "GeneralForumTopicHidden",
    "ReplyKeyboardRemove",
    "KeyboardButtonRequestChat",
    "ForumTopic",
    "InlineQueryResult",
    "InlineQueryResultArticle",
    "InlineQueryResultAudio",
    "InlineQueryResultCachedAudio",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultContact",
    "InlineQueryResultDocument",
    "InlineQueryResultGame",
    "InlineQueryResultGif",
    "InlineQueryResultLocation",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultPhoto",
    "InlineQueryResultVenue",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
    "ReplyParameters",
    "PollAnswer",
    "ProximityAlertTriggered",
    "ChatBoostSource",
    "ChatBoostSourceGiftCode",
    "ChatBoostSourceGiveaway",
    "ChatBoostSourcePremium",
    "MessageAutoDeleteTimerChanged",
    "Voice",
    "VideoChatEnded",
    "BotCommandScope",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "BotCommandScopeDefault",
    "User",
    "PollOption",
    "WebAppInfo",
    "VideoChatParticipantsInvited",
    "ForceReply",
    "ChatInviteLink",
    "Dice",
    "EncryptedCredentials",
    "Invoice",
    "PassportData",
    "BotShortDescription",
    "ReplyKeyboardMarkup",
    "ChatBoostRemoved",
    "Game",
    "ShippingAddress",
    "File",
    "GiveawayCreated",
    "SwitchInlineQueryChosenChat",
    "ShippingOption",
    "Chat",
    "KeyboardButtonPollType",
    "GiveawayWinners",
    "ReactionType",
    "ReactionTypeCustomEmoji",
    "ReactionTypeEmoji",
    "UsersShared",
    "KeyboardButton",
    "KeyboardButtonRequestUsers",
    "PassportFile",
    "ForumTopicClosed",
    "ChatJoinRequest",
]
