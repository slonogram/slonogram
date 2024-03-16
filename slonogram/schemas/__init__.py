from slonogram.schemas.chat_boost_updated import ChatBoostUpdated
from slonogram.schemas.video_chat_participants_invited import (
    VideoChatParticipantsInvited,
)
from slonogram.schemas.passport_data import PassportData
from slonogram.schemas.login_url import LoginUrl
from slonogram.schemas.poll_option import PollOption
from slonogram.schemas.reply_keyboard_remove import ReplyKeyboardRemove
from slonogram.schemas.message_reaction_updated import MessageReactionUpdated
from slonogram.schemas.switch_inline_query_chosen_chat import (
    SwitchInlineQueryChosenChat,
)
from slonogram.schemas.chat_invite_link import ChatInviteLink
from slonogram.schemas.keyboard_button_request_users import KeyboardButtonRequestUsers
from slonogram.schemas.general_forum_topic_unhidden import GeneralForumTopicUnhidden
from slonogram.schemas.external_reply_info import ExternalReplyInfo
from slonogram.schemas.chat_join_request import ChatJoinRequest
from slonogram.schemas.shipping_query import ShippingQuery
from slonogram.schemas.write_access_allowed import WriteAccessAllowed
from slonogram.schemas.user_profile_photos import UserProfilePhotos
from slonogram.schemas.chat import Chat
from slonogram.schemas.menu_button import (
    MenuButtonCommands,
    MenuButtonDefault,
    MenuButtonWebApp,
    MenuButton,
)
from slonogram.schemas.shipping_option import ShippingOption
from slonogram.schemas.passport_element_error import (
    PassportElementErrorDataField,
    PassportElementErrorFile,
    PassportElementErrorFiles,
    PassportElementErrorFrontSide,
    PassportElementErrorReverseSide,
    PassportElementErrorSelfie,
    PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified,
    PassportElementError,
)
from slonogram.schemas.photo_size import PhotoSize
from slonogram.schemas.reply_parameters import ReplyParameters
from slonogram.schemas.inline_keyboard_markup import InlineKeyboardMarkup
from slonogram.schemas.input_sticker import InputSticker
from slonogram.schemas.forum_topic_created import ForumTopicCreated
from slonogram.schemas.forum_topic_closed import ForumTopicClosed
from slonogram.schemas.link_preview_options import LinkPreviewOptions
from slonogram.schemas.poll_answer import PollAnswer
from slonogram.schemas.callback_game import CallbackGame
from slonogram.schemas.giveaway_created import GiveawayCreated
from slonogram.schemas.bot_command import BotCommand
from slonogram.schemas.text_quote import TextQuote
from slonogram.schemas.game_high_score import GameHighScore
from slonogram.schemas.encrypted_credentials import EncryptedCredentials
from slonogram.schemas.message_origin import (
    MessageOriginChannel,
    MessageOriginChat,
    MessageOriginHiddenUser,
    MessageOriginUser,
    MessageOrigin,
)
from slonogram.schemas.animation import Animation
from slonogram.schemas.message_entity import MessageEntity
from slonogram.schemas.input_media import (
    InputMediaAnimation,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    InputMedia,
)
from slonogram.schemas.keyboard_button_request_chat import KeyboardButtonRequestChat
from slonogram.schemas.webhook_info import WebhookInfo
from slonogram.schemas.chat_boost_source import (
    ChatBoostSourceGiftCode,
    ChatBoostSourceGiveaway,
    ChatBoostSourcePremium,
    ChatBoostSource,
)
from slonogram.schemas.chat_boost_added import ChatBoostAdded
from slonogram.schemas.general_forum_topic_hidden import GeneralForumTopicHidden
from slonogram.schemas.proximity_alert_triggered import ProximityAlertTriggered
from slonogram.schemas.bot_short_description import BotShortDescription
from slonogram.schemas.location import Location
from slonogram.schemas.keyboard_button_poll_type import KeyboardButtonPollType
from slonogram.schemas.chat_boost_removed import ChatBoostRemoved
from slonogram.schemas.chat_location import ChatLocation
from slonogram.schemas.input_message_content import (
    InputContactMessageContent,
    InputInvoiceMessageContent,
    InputLocationMessageContent,
    InputTextMessageContent,
    InputVenueMessageContent,
    InputMessageContent,
)
from slonogram.schemas.file import File
from slonogram.schemas.force_reply import ForceReply
from slonogram.schemas.chosen_inline_result import ChosenInlineResult
from slonogram.schemas.successful_payment import SuccessfulPayment
from slonogram.schemas.game import Game
from slonogram.schemas.video_chat_ended import VideoChatEnded
from slonogram.schemas.chat_member_updated import ChatMemberUpdated
from slonogram.schemas.input_file import InputFile
from slonogram.schemas.reaction_count import ReactionCount
from slonogram.schemas.chat_shared import ChatShared
from slonogram.schemas.reaction_type import (
    ReactionTypeCustomEmoji,
    ReactionTypeEmoji,
    ReactionType,
)
from slonogram.schemas.giveaway_completed import GiveawayCompleted
from slonogram.schemas.order_info import OrderInfo
from slonogram.schemas.message_auto_delete_timer_changed import (
    MessageAutoDeleteTimerChanged,
)
from slonogram.schemas.encrypted_passport_element import EncryptedPassportElement
from slonogram.schemas.callback_query import CallbackQuery
from slonogram.schemas.video import Video
from slonogram.schemas.bot_command_scope import (
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
    BotCommandScopeDefault,
    BotCommandScope,
)
from slonogram.schemas.inline_query import InlineQuery
from slonogram.schemas.bot_description import BotDescription
from slonogram.schemas.giveaway_winners import GiveawayWinners
from slonogram.schemas.forum_topic_edited import ForumTopicEdited
from slonogram.schemas.story import Story
from slonogram.schemas.message_reaction_count_updated import MessageReactionCountUpdated
from slonogram.schemas.chat_boost import ChatBoost
from slonogram.schemas.dice import Dice
from slonogram.schemas.user import User
from slonogram.schemas.chat_member import (
    ChatMemberAdministrator,
    ChatMemberBanned,
    ChatMemberLeft,
    ChatMemberMember,
    ChatMemberOwner,
    ChatMemberRestricted,
    ChatMember,
)
from slonogram.schemas.document import Document
from slonogram.schemas.keyboard_button import KeyboardButton
from slonogram.schemas.users_shared import UsersShared
from slonogram.schemas.sent_web_app_message import SentWebAppMessage
from slonogram.schemas.voice import Voice
from slonogram.schemas.reply_keyboard_markup import ReplyKeyboardMarkup
from slonogram.schemas.chat_permissions import ChatPermissions
from slonogram.schemas.mask_position import MaskPosition
from slonogram.schemas.inline_keyboard_button import InlineKeyboardButton
from slonogram.schemas.video_chat_scheduled import VideoChatScheduled
from slonogram.schemas.giveaway import Giveaway
from slonogram.schemas.bot_name import BotName
from slonogram.schemas.poll import Poll
from slonogram.schemas.video_chat_started import VideoChatStarted
from slonogram.schemas.maybe_inaccessible_message import (
    InaccessibleMessage,
    Message,
    MaybeInaccessibleMessage,
)
from slonogram.schemas.web_app_data import WebAppData
from slonogram.schemas.video_note import VideoNote
from slonogram.schemas.chat_photo import ChatPhoto
from slonogram.schemas.labeled_price import LabeledPrice
from slonogram.schemas.chat_administrator_rights import ChatAdministratorRights
from slonogram.schemas.inline_query_result import (
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
    InlineQueryResult,
)
from slonogram.schemas.passport_file import PassportFile
from slonogram.schemas.message_id import MessageId
from slonogram.schemas.response_parameters import ResponseParameters
from slonogram.schemas.forum_topic import ForumTopic
from slonogram.schemas.user_chat_boosts import UserChatBoosts
from slonogram.schemas.audio import Audio
from slonogram.schemas.sticker_set import StickerSet
from slonogram.schemas.pre_checkout_query import PreCheckoutQuery
from slonogram.schemas.shipping_address import ShippingAddress
from slonogram.schemas.sticker import Sticker
from slonogram.schemas.venue import Venue
from slonogram.schemas.web_app_info import WebAppInfo
from slonogram.schemas.contact import Contact
from slonogram.schemas.invoice import Invoice
from slonogram.schemas.update import Update
from slonogram.schemas.inline_query_results_button import InlineQueryResultsButton
from slonogram.schemas.forum_topic_reopened import ForumTopicReopened

__all__ = [
    "ChatBoostUpdated",
    "VideoChatParticipantsInvited",
    "PassportData",
    "LoginUrl",
    "PollOption",
    "ReplyKeyboardRemove",
    "MessageReactionUpdated",
    "SwitchInlineQueryChosenChat",
    "ChatInviteLink",
    "KeyboardButtonRequestUsers",
    "GeneralForumTopicUnhidden",
    "ExternalReplyInfo",
    "ChatJoinRequest",
    "ShippingQuery",
    "WriteAccessAllowed",
    "UserProfilePhotos",
    "Chat",
    "MenuButtonCommands",
    "MenuButtonDefault",
    "MenuButtonWebApp",
    "MenuButton",
    "ShippingOption",
    "PassportElementErrorDataField",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "PassportElementError",
    "PhotoSize",
    "ReplyParameters",
    "InlineKeyboardMarkup",
    "InputSticker",
    "ForumTopicCreated",
    "ForumTopicClosed",
    "LinkPreviewOptions",
    "PollAnswer",
    "CallbackGame",
    "GiveawayCreated",
    "BotCommand",
    "TextQuote",
    "GameHighScore",
    "EncryptedCredentials",
    "MessageOriginChannel",
    "MessageOriginChat",
    "MessageOriginHiddenUser",
    "MessageOriginUser",
    "MessageOrigin",
    "Animation",
    "MessageEntity",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMedia",
    "KeyboardButtonRequestChat",
    "WebhookInfo",
    "ChatBoostSourceGiftCode",
    "ChatBoostSourceGiveaway",
    "ChatBoostSourcePremium",
    "ChatBoostSource",
    "ChatBoostAdded",
    "GeneralForumTopicHidden",
    "ProximityAlertTriggered",
    "BotShortDescription",
    "Location",
    "KeyboardButtonPollType",
    "ChatBoostRemoved",
    "ChatLocation",
    "InputContactMessageContent",
    "InputInvoiceMessageContent",
    "InputLocationMessageContent",
    "InputTextMessageContent",
    "InputVenueMessageContent",
    "InputMessageContent",
    "File",
    "ForceReply",
    "ChosenInlineResult",
    "SuccessfulPayment",
    "Game",
    "VideoChatEnded",
    "ChatMemberUpdated",
    "InputFile",
    "ReactionCount",
    "ChatShared",
    "ReactionTypeCustomEmoji",
    "ReactionTypeEmoji",
    "ReactionType",
    "GiveawayCompleted",
    "OrderInfo",
    "MessageAutoDeleteTimerChanged",
    "EncryptedPassportElement",
    "CallbackQuery",
    "Video",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "BotCommandScopeDefault",
    "BotCommandScope",
    "InlineQuery",
    "BotDescription",
    "GiveawayWinners",
    "ForumTopicEdited",
    "Story",
    "MessageReactionCountUpdated",
    "ChatBoost",
    "Dice",
    "User",
    "ChatMemberAdministrator",
    "ChatMemberBanned",
    "ChatMemberLeft",
    "ChatMemberMember",
    "ChatMemberOwner",
    "ChatMemberRestricted",
    "ChatMember",
    "Document",
    "KeyboardButton",
    "UsersShared",
    "SentWebAppMessage",
    "Voice",
    "ReplyKeyboardMarkup",
    "ChatPermissions",
    "MaskPosition",
    "InlineKeyboardButton",
    "VideoChatScheduled",
    "Giveaway",
    "BotName",
    "Poll",
    "VideoChatStarted",
    "InaccessibleMessage",
    "Message",
    "MaybeInaccessibleMessage",
    "WebAppData",
    "VideoNote",
    "ChatPhoto",
    "LabeledPrice",
    "ChatAdministratorRights",
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
    "InlineQueryResult",
    "PassportFile",
    "MessageId",
    "ResponseParameters",
    "ForumTopic",
    "UserChatBoosts",
    "Audio",
    "StickerSet",
    "PreCheckoutQuery",
    "ShippingAddress",
    "Sticker",
    "Venue",
    "WebAppInfo",
    "Contact",
    "Invoice",
    "Update",
    "InlineQueryResultsButton",
    "ForumTopicReopened",
]
