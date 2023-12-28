from slonogram.session import Session
from adaptix import Retort
from slonogram.schemas import (
    PassportElementError,
    MenuButton,
    ChatPermissions,
    ChatMember,
    GameHighScore,
    InputMedia,
    Chat,
    Message,
    MaskPosition,
    ShippingOption,
    ChatInviteLink,
    InlineQueryResult,
    MessageId,
    BotDescription,
    BotShortDescription,
    StickerSet,
    ForceReply,
    ReplyKeyboardRemove,
    Poll,
    User,
    File,
    InputMediaVideo,
    UserProfilePhotos,
    SentWebAppMessage,
    MessageEntity,
    BotName,
    ReplyKeyboardMarkup,
    ForumTopic,
    BotCommand,
    InputSticker,
    WebhookInfo,
    Sticker,
    ChatAdministratorRights,
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InputMediaDocument,
    Update,
    LabeledPrice,
    InputMediaAudio,
    BotCommandScope,
    InlineQueryResultsButton,
)
from slonogram.methods.get_updates import GetUpdates
from io import IOBase
from slonogram.methods.set_webhook import SetWebhook
from slonogram.methods.delete_webhook import DeleteWebhook
from slonogram.methods.get_webhook_info import GetWebhookInfo
from slonogram.methods.get_me import GetMe
from slonogram.methods.log_out import LogOut
from slonogram.methods.close import Close
from slonogram.methods.send_message import SendMessage
from slonogram.methods.forward_message import ForwardMessage
from slonogram.methods.copy_message import CopyMessage
from slonogram.methods.send_photo import SendPhoto
from slonogram.methods.send_audio import SendAudio
from slonogram.methods.send_document import SendDocument
from slonogram.methods.send_video import SendVideo
from slonogram.methods.send_animation import SendAnimation
from slonogram.methods.send_voice import SendVoice
from slonogram.methods.send_video_note import SendVideoNote
from slonogram.methods.send_media_group import SendMediaGroup
from slonogram.methods.send_location import SendLocation
from slonogram.methods.send_venue import SendVenue
from slonogram.methods.send_contact import SendContact
from slonogram.methods.send_poll import SendPoll
from slonogram.methods.send_dice import SendDice
from slonogram.methods.send_chat_action import SendChatAction
from slonogram.methods.get_user_profile_photos import GetUserProfilePhotos
from slonogram.methods.get_file import GetFile
from slonogram.methods.ban_chat_member import BanChatMember
from slonogram.methods.unban_chat_member import UnbanChatMember
from slonogram.methods.restrict_chat_member import RestrictChatMember
from slonogram.methods.promote_chat_member import PromoteChatMember
from slonogram.methods.set_chat_administrator_custom_title import (
    SetChatAdministratorCustomTitle,
)
from slonogram.methods.ban_chat_sender_chat import BanChatSenderChat
from slonogram.methods.unban_chat_sender_chat import UnbanChatSenderChat
from slonogram.methods.set_chat_permissions import SetChatPermissions
from slonogram.methods.export_chat_invite_link import ExportChatInviteLink
from slonogram.methods.create_chat_invite_link import CreateChatInviteLink
from slonogram.methods.edit_chat_invite_link import EditChatInviteLink
from slonogram.methods.revoke_chat_invite_link import RevokeChatInviteLink
from slonogram.methods.approve_chat_join_request import ApproveChatJoinRequest
from slonogram.methods.decline_chat_join_request import DeclineChatJoinRequest
from slonogram.methods.set_chat_photo import SetChatPhoto
from slonogram.methods.delete_chat_photo import DeleteChatPhoto
from slonogram.methods.set_chat_title import SetChatTitle
from slonogram.methods.set_chat_description import SetChatDescription
from slonogram.methods.pin_chat_message import PinChatMessage
from slonogram.methods.unpin_chat_message import UnpinChatMessage
from slonogram.methods.unpin_all_chat_messages import UnpinAllChatMessages
from slonogram.methods.leave_chat import LeaveChat
from slonogram.methods.get_chat import GetChat
from slonogram.methods.get_chat_administrators import GetChatAdministrators
from slonogram.methods.get_chat_member_count import GetChatMemberCount
from slonogram.methods.get_chat_member import GetChatMember
from slonogram.methods.set_chat_sticker_set import SetChatStickerSet
from slonogram.methods.delete_chat_sticker_set import DeleteChatStickerSet
from slonogram.methods.get_forum_topic_icon_stickers import GetForumTopicIconStickers
from slonogram.methods.create_forum_topic import CreateForumTopic
from slonogram.methods.edit_forum_topic import EditForumTopic
from slonogram.methods.close_forum_topic import CloseForumTopic
from slonogram.methods.reopen_forum_topic import ReopenForumTopic
from slonogram.methods.delete_forum_topic import DeleteForumTopic
from slonogram.methods.unpin_all_forum_topic_messages import UnpinAllForumTopicMessages
from slonogram.methods.edit_general_forum_topic import EditGeneralForumTopic
from slonogram.methods.close_general_forum_topic import CloseGeneralForumTopic
from slonogram.methods.reopen_general_forum_topic import ReopenGeneralForumTopic
from slonogram.methods.hide_general_forum_topic import HideGeneralForumTopic
from slonogram.methods.unhide_general_forum_topic import UnhideGeneralForumTopic
from slonogram.methods.unpin_all_general_forum_topic_messages import (
    UnpinAllGeneralForumTopicMessages,
)
from slonogram.methods.answer_callback_query import AnswerCallbackQuery
from slonogram.methods.set_my_commands import SetMyCommands
from slonogram.methods.delete_my_commands import DeleteMyCommands
from slonogram.methods.get_my_commands import GetMyCommands
from slonogram.methods.set_my_name import SetMyName
from slonogram.methods.get_my_name import GetMyName
from slonogram.methods.set_my_description import SetMyDescription
from slonogram.methods.get_my_description import GetMyDescription
from slonogram.methods.set_my_short_description import SetMyShortDescription
from slonogram.methods.get_my_short_description import GetMyShortDescription
from slonogram.methods.set_chat_menu_button import SetChatMenuButton
from slonogram.methods.get_chat_menu_button import GetChatMenuButton
from slonogram.methods.set_my_default_administrator_rights import (
    SetMyDefaultAdministratorRights,
)
from slonogram.methods.get_my_default_administrator_rights import (
    GetMyDefaultAdministratorRights,
)
from slonogram.methods.edit_message_text import EditMessageText
from slonogram.methods.edit_message_caption import EditMessageCaption
from slonogram.methods.edit_message_media import EditMessageMedia
from slonogram.methods.edit_message_live_location import EditMessageLiveLocation
from slonogram.methods.stop_message_live_location import StopMessageLiveLocation
from slonogram.methods.edit_message_reply_markup import EditMessageReplyMarkup
from slonogram.methods.stop_poll import StopPoll
from slonogram.methods.delete_message import DeleteMessage
from slonogram.methods.send_sticker import SendSticker
from slonogram.methods.get_sticker_set import GetStickerSet
from slonogram.methods.get_custom_emoji_stickers import GetCustomEmojiStickers
from slonogram.methods.upload_sticker_file import UploadStickerFile
from slonogram.methods.create_new_sticker_set import CreateNewStickerSet
from slonogram.methods.add_sticker_to_set import AddStickerToSet
from slonogram.methods.set_sticker_position_in_set import SetStickerPositionInSet
from slonogram.methods.delete_sticker_from_set import DeleteStickerFromSet
from slonogram.methods.set_sticker_emoji_list import SetStickerEmojiList
from slonogram.methods.set_sticker_keywords import SetStickerKeywords
from slonogram.methods.set_sticker_mask_position import SetStickerMaskPosition
from slonogram.methods.set_sticker_set_title import SetStickerSetTitle
from slonogram.methods.set_sticker_set_thumbnail import SetStickerSetThumbnail
from slonogram.methods.set_custom_emoji_sticker_set_thumbnail import (
    SetCustomEmojiStickerSetThumbnail,
)
from slonogram.methods.delete_sticker_set import DeleteStickerSet
from slonogram.methods.answer_inline_query import AnswerInlineQuery
from slonogram.methods.answer_web_app_query import AnswerWebAppQuery
from slonogram.methods.send_invoice import SendInvoice
from slonogram.methods.create_invoice_link import CreateInvoiceLink
from slonogram.methods.answer_shipping_query import AnswerShippingQuery
from slonogram.methods.answer_pre_checkout_query import AnswerPreCheckoutQuery
from slonogram.methods.set_passport_data_errors import SetPassportDataErrors
from slonogram.methods.send_game import SendGame
from slonogram.methods.set_game_score import SetGameScore
from slonogram.methods.get_game_high_scores import GetGameHighScores


class MethodsWrapper:
    """Wrapper for calling the methods"""

    def __init__(
        self,
        session: Session,
        retort: Retort,
    ) -> None:
        self.session = session
        self.retort = retort

    async def get_updates(
        self,
        offset: int | None = None,
        limit: int | None = None,
        timeout: int | None = None,
        allowed_updates: list[str] | None = None,
    ) -> list[Update]:
        """Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects."""
        return self.retort.load(
            await self.session.call_method(
                "getUpdates", GetUpdates(offset, limit, timeout, allowed_updates)
            ),
            list[Update],
        )

    async def set_webhook(
        self,
        url: str,
        certificate: IOBase | None = None,
        ip_address: str | None = None,
        max_connections: int | None = None,
        allowed_updates: list[str] | None = None,
        drop_pending_updates: bool | None = None,
        secret_token: str | None = None,
    ) -> bool:
        """Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success.
        If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header "X-Telegram-Bot-Api-Secret-Token" with the secret token as content.
        """
        return self.retort.load(
            await self.session.call_method(
                "setWebhook",
                SetWebhook(
                    url,
                    certificate,
                    ip_address,
                    max_connections,
                    allowed_updates,
                    drop_pending_updates,
                    secret_token,
                ),
            ),
            bool,
        )

    async def delete_webhook(self, drop_pending_updates: bool | None = None) -> bool:
        """Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "deleteWebhook", DeleteWebhook(drop_pending_updates)
            ),
            bool,
        )

    async def get_webhook_info(self) -> WebhookInfo:
        """Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty."""
        return self.retort.load(
            await self.session.call_method("getWebhookInfo", GetWebhookInfo()),
            WebhookInfo,
        )

    async def get_me(self) -> User:
        """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object."""
        return self.retort.load(await self.session.call_method("getMe", GetMe()), User)

    async def log_out(self) -> bool:
        """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
        return self.retort.load(
            await self.session.call_method("logOut", LogOut()), bool
        )

    async def close(self) -> bool:
        """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
        return self.retort.load(await self.session.call_method("close", Close()), bool)

    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        message_thread_id: int | None = None,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        disable_web_page_preview: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send text messages. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendMessage",
                SendMessage(
                    chat_id,
                    text,
                    message_thread_id,
                    parse_mode,
                    entities,
                    disable_web_page_preview,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def forward_message(
        self,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
    ) -> Message:
        """Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "forwardMessage",
                ForwardMessage(
                    chat_id,
                    from_chat_id,
                    message_id,
                    message_thread_id,
                    disable_notification,
                    protect_content,
                ),
            ),
            Message,
        )

    async def copy_message(
        self,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> MessageId:
        """Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success."""
        return self.retort.load(
            await self.session.call_method(
                "copyMessage",
                CopyMessage(
                    chat_id,
                    from_chat_id,
                    message_id,
                    message_thread_id,
                    caption,
                    parse_mode,
                    caption_entities,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            MessageId,
        )

    async def send_photo(
        self,
        chat_id: int | str,
        photo: IOBase | str,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send photos. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendPhoto",
                SendPhoto(
                    chat_id,
                    photo,
                    message_thread_id,
                    caption,
                    parse_mode,
                    caption_entities,
                    has_spoiler,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_audio(
        self,
        chat_id: int | str,
        audio: IOBase | str,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        duration: int | None = None,
        performer: str | None = None,
        title: str | None = None,
        thumbnail: IOBase | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the sendVoice method instead.
        """
        return self.retort.load(
            await self.session.call_method(
                "sendAudio",
                SendAudio(
                    chat_id,
                    audio,
                    message_thread_id,
                    caption,
                    parse_mode,
                    caption_entities,
                    duration,
                    performer,
                    title,
                    thumbnail,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_document(
        self,
        chat_id: int | str,
        document: IOBase | str,
        message_thread_id: int | None = None,
        thumbnail: IOBase | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        disable_content_type_detection: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future."""
        return self.retort.load(
            await self.session.call_method(
                "sendDocument",
                SendDocument(
                    chat_id,
                    document,
                    message_thread_id,
                    thumbnail,
                    caption,
                    parse_mode,
                    caption_entities,
                    disable_content_type_detection,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_video(
        self,
        chat_id: int | str,
        video: IOBase | str,
        message_thread_id: int | None = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: IOBase | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        supports_streaming: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future."""
        return self.retort.load(
            await self.session.call_method(
                "sendVideo",
                SendVideo(
                    chat_id,
                    video,
                    message_thread_id,
                    duration,
                    width,
                    height,
                    thumbnail,
                    caption,
                    parse_mode,
                    caption_entities,
                    has_spoiler,
                    supports_streaming,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_animation(
        self,
        chat_id: int | str,
        animation: IOBase | str,
        message_thread_id: int | None = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: IOBase | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future."""
        return self.retort.load(
            await self.session.call_method(
                "sendAnimation",
                SendAnimation(
                    chat_id,
                    animation,
                    message_thread_id,
                    duration,
                    width,
                    height,
                    thumbnail,
                    caption,
                    parse_mode,
                    caption_entities,
                    has_spoiler,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_voice(
        self,
        chat_id: int | str,
        voice: IOBase | str,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future."""
        return self.retort.load(
            await self.session.call_method(
                "sendVoice",
                SendVoice(
                    chat_id,
                    voice,
                    message_thread_id,
                    caption,
                    parse_mode,
                    caption_entities,
                    duration,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_video_note(
        self,
        chat_id: int | str,
        video_note: IOBase | str,
        message_thread_id: int | None = None,
        duration: int | None = None,
        length: int | None = None,
        thumbnail: IOBase | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendVideoNote",
                SendVideoNote(
                    chat_id,
                    video_note,
                    message_thread_id,
                    duration,
                    length,
                    thumbnail,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_media_group(
        self,
        chat_id: int | str,
        media: list[InputMediaAudio]
        | list[InputMediaDocument]
        | list[InputMediaPhoto]
        | list[InputMediaVideo],
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
    ) -> list[Message]:
        """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendMediaGroup",
                SendMediaGroup(
                    chat_id,
                    media,
                    message_thread_id,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                ),
            ),
            list[Message],
        )

    async def send_location(
        self,
        chat_id: int | str,
        latitude: float,
        longitude: float,
        message_thread_id: int | None = None,
        horizontal_accuracy: float | None = None,
        live_period: int | None = None,
        heading: int | None = None,
        proximity_alert_radius: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send point on the map. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendLocation",
                SendLocation(
                    chat_id,
                    latitude,
                    longitude,
                    message_thread_id,
                    horizontal_accuracy,
                    live_period,
                    heading,
                    proximity_alert_radius,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_venue(
        self,
        chat_id: int | str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        message_thread_id: int | None = None,
        foursquare_id: str | None = None,
        foursquare_type: str | None = None,
        google_place_id: str | None = None,
        google_place_type: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send information about a venue. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendVenue",
                SendVenue(
                    chat_id,
                    latitude,
                    longitude,
                    title,
                    address,
                    message_thread_id,
                    foursquare_id,
                    foursquare_type,
                    google_place_id,
                    google_place_type,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_contact(
        self,
        chat_id: int | str,
        phone_number: str,
        first_name: str,
        message_thread_id: int | None = None,
        last_name: str | None = None,
        vcard: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send phone contacts. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendContact",
                SendContact(
                    chat_id,
                    phone_number,
                    first_name,
                    message_thread_id,
                    last_name,
                    vcard,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_poll(
        self,
        chat_id: int | str,
        question: str,
        options: list[str],
        message_thread_id: int | None = None,
        is_anonymous: bool | None = None,
        type: str | None = None,
        allows_multiple_answers: bool | None = None,
        correct_option_id: int | None = None,
        explanation: str | None = None,
        explanation_parse_mode: str | None = None,
        explanation_entities: list[MessageEntity] | None = None,
        open_period: int | None = None,
        close_date: int | None = None,
        is_closed: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send a native poll. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendPoll",
                SendPoll(
                    chat_id,
                    question,
                    options,
                    message_thread_id,
                    is_anonymous,
                    type,
                    allows_multiple_answers,
                    correct_option_id,
                    explanation,
                    explanation_parse_mode,
                    explanation_entities,
                    open_period,
                    close_date,
                    is_closed,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_dice(
        self,
        chat_id: int | str,
        message_thread_id: int | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendDice",
                SendDice(
                    chat_id,
                    message_thread_id,
                    emoji,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def send_chat_action(
        self, chat_id: int | str, action: str, message_thread_id: int | None = None
    ) -> bool:
        """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.
        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.
        """
        return self.retort.load(
            await self.session.call_method(
                "sendChatAction", SendChatAction(chat_id, action, message_thread_id)
            ),
            bool,
        )

    async def get_user_profile_photos(
        self, user_id: int, offset: int | None = None, limit: int | None = None
    ) -> UserProfilePhotos:
        """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object."""
        return self.retort.load(
            await self.session.call_method(
                "getUserProfilePhotos", GetUserProfilePhotos(user_id, offset, limit)
            ),
            UserProfilePhotos,
        )

    async def get_file(self, file_id: str) -> File:
        """Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.
        Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received.
        """
        return self.retort.load(
            await self.session.call_method("getFile", GetFile(file_id)), File
        )

    async def ban_chat_member(
        self,
        chat_id: int | str,
        user_id: int,
        until_date: int | None = None,
        revoke_messages: bool | None = None,
    ) -> bool:
        """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "banChatMember",
                BanChatMember(chat_id, user_id, until_date, revoke_messages),
            ),
            bool,
        )

    async def unban_chat_member(
        self, chat_id: int | str, user_id: int, only_if_banned: bool | None = None
    ) -> bool:
        """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "unbanChatMember", UnbanChatMember(chat_id, user_id, only_if_banned)
            ),
            bool,
        )

    async def restrict_chat_member(
        self,
        chat_id: int | str,
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool | None = None,
        until_date: int | None = None,
    ) -> bool:
        """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "restrictChatMember",
                RestrictChatMember(
                    chat_id,
                    user_id,
                    permissions,
                    use_independent_chat_permissions,
                    until_date,
                ),
            ),
            bool,
        )

    async def promote_chat_member(
        self,
        chat_id: int | str,
        user_id: int,
        is_anonymous: bool | None = None,
        can_manage_chat: bool | None = None,
        can_delete_messages: bool | None = None,
        can_manage_video_chats: bool | None = None,
        can_restrict_members: bool | None = None,
        can_promote_members: bool | None = None,
        can_change_info: bool | None = None,
        can_invite_users: bool | None = None,
        can_post_messages: bool | None = None,
        can_edit_messages: bool | None = None,
        can_pin_messages: bool | None = None,
        can_post_stories: bool | None = None,
        can_edit_stories: bool | None = None,
        can_delete_stories: bool | None = None,
        can_manage_topics: bool | None = None,
    ) -> bool:
        """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "promoteChatMember",
                PromoteChatMember(
                    chat_id,
                    user_id,
                    is_anonymous,
                    can_manage_chat,
                    can_delete_messages,
                    can_manage_video_chats,
                    can_restrict_members,
                    can_promote_members,
                    can_change_info,
                    can_invite_users,
                    can_post_messages,
                    can_edit_messages,
                    can_pin_messages,
                    can_post_stories,
                    can_edit_stories,
                    can_delete_stories,
                    can_manage_topics,
                ),
            ),
            bool,
        )

    async def set_chat_administrator_custom_title(
        self, chat_id: int | str, user_id: int, custom_title: str
    ) -> bool:
        """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setChatAdministratorCustomTitle",
                SetChatAdministratorCustomTitle(chat_id, user_id, custom_title),
            ),
            bool,
        )

    async def ban_chat_sender_chat(
        self, chat_id: int | str, sender_chat_id: int
    ) -> bool:
        """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "banChatSenderChat", BanChatSenderChat(chat_id, sender_chat_id)
            ),
            bool,
        )

    async def unban_chat_sender_chat(
        self, chat_id: int | str, sender_chat_id: int
    ) -> bool:
        """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "unbanChatSenderChat", UnbanChatSenderChat(chat_id, sender_chat_id)
            ),
            bool,
        )

    async def set_chat_permissions(
        self,
        chat_id: int | str,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool | None = None,
    ) -> bool:
        """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setChatPermissions",
                SetChatPermissions(
                    chat_id, permissions, use_independent_chat_permissions
                ),
            ),
            bool,
        )

    async def export_chat_invite_link(self, chat_id: int | str) -> str:
        """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success."""
        return self.retort.load(
            await self.session.call_method(
                "exportChatInviteLink", ExportChatInviteLink(chat_id)
            ),
            str,
        )

    async def create_chat_invite_link(
        self,
        chat_id: int | str,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        creates_join_request: bool | None = None,
    ) -> ChatInviteLink:
        """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object."""
        return self.retort.load(
            await self.session.call_method(
                "createChatInviteLink",
                CreateChatInviteLink(
                    chat_id, name, expire_date, member_limit, creates_join_request
                ),
            ),
            ChatInviteLink,
        )

    async def edit_chat_invite_link(
        self,
        chat_id: int | str,
        invite_link: str,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        creates_join_request: bool | None = None,
    ) -> ChatInviteLink:
        """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object."""
        return self.retort.load(
            await self.session.call_method(
                "editChatInviteLink",
                EditChatInviteLink(
                    chat_id,
                    invite_link,
                    name,
                    expire_date,
                    member_limit,
                    creates_join_request,
                ),
            ),
            ChatInviteLink,
        )

    async def revoke_chat_invite_link(
        self, chat_id: int | str, invite_link: str
    ) -> ChatInviteLink:
        """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object."""
        return self.retort.load(
            await self.session.call_method(
                "revokeChatInviteLink", RevokeChatInviteLink(chat_id, invite_link)
            ),
            ChatInviteLink,
        )

    async def approve_chat_join_request(self, chat_id: int | str, user_id: int) -> bool:
        """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "approveChatJoinRequest", ApproveChatJoinRequest(chat_id, user_id)
            ),
            bool,
        )

    async def decline_chat_join_request(self, chat_id: int | str, user_id: int) -> bool:
        """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "declineChatJoinRequest", DeclineChatJoinRequest(chat_id, user_id)
            ),
            bool,
        )

    async def set_chat_photo(self, chat_id: int | str, photo: IOBase) -> bool:
        """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setChatPhoto", SetChatPhoto(chat_id, photo)
            ),
            bool,
        )

    async def delete_chat_photo(self, chat_id: int | str) -> bool:
        """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method("deleteChatPhoto", DeleteChatPhoto(chat_id)),
            bool,
        )

    async def set_chat_title(self, chat_id: int | str, title: str) -> bool:
        """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setChatTitle", SetChatTitle(chat_id, title)
            ),
            bool,
        )

    async def set_chat_description(
        self, chat_id: int | str, description: str | None = None
    ) -> bool:
        """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setChatDescription", SetChatDescription(chat_id, description)
            ),
            bool,
        )

    async def pin_chat_message(
        self,
        chat_id: int | str,
        message_id: int,
        disable_notification: bool | None = None,
    ) -> bool:
        """Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "pinChatMessage",
                PinChatMessage(chat_id, message_id, disable_notification),
            ),
            bool,
        )

    async def unpin_chat_message(
        self, chat_id: int | str, message_id: int | None = None
    ) -> bool:
        """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "unpinChatMessage", UnpinChatMessage(chat_id, message_id)
            ),
            bool,
        )

    async def unpin_all_chat_messages(self, chat_id: int | str) -> bool:
        """Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "unpinAllChatMessages", UnpinAllChatMessages(chat_id)
            ),
            bool,
        )

    async def leave_chat(self, chat_id: int | str) -> bool:
        """Use this method for your bot to leave a group, supergroup or channel. Returns True on success."""
        return self.retort.load(
            await self.session.call_method("leaveChat", LeaveChat(chat_id)), bool
        )

    async def get_chat(self, chat_id: int | str) -> Chat:
        """Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success."""
        return self.retort.load(
            await self.session.call_method("getChat", GetChat(chat_id)), Chat
        )

    async def get_chat_administrators(self, chat_id: int | str) -> list[ChatMember]:
        """Use this method to get a list of administrators in a chat, which aren't bots. Returns an Array of ChatMember objects."""
        return self.retort.load(
            await self.session.call_method(
                "getChatAdministrators", GetChatAdministrators(chat_id)
            ),
            list[ChatMember],
        )

    async def get_chat_member_count(self, chat_id: int | str) -> int:
        """Use this method to get the number of members in a chat. Returns Int on success."""
        return self.retort.load(
            await self.session.call_method(
                "getChatMemberCount", GetChatMemberCount(chat_id)
            ),
            int,
        )

    async def get_chat_member(self, chat_id: int | str, user_id: int) -> ChatMember:
        """Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success."""
        return self.retort.load(
            await self.session.call_method(
                "getChatMember", GetChatMember(chat_id, user_id)
            ),
            ChatMember,
        )

    async def set_chat_sticker_set(
        self, chat_id: int | str, sticker_set_name: str
    ) -> bool:
        """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setChatStickerSet", SetChatStickerSet(chat_id, sticker_set_name)
            ),
            bool,
        )

    async def delete_chat_sticker_set(self, chat_id: int | str) -> bool:
        """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "deleteChatStickerSet", DeleteChatStickerSet(chat_id)
            ),
            bool,
        )

    async def get_forum_topic_icon_stickers(self) -> list[Sticker]:
        """Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of Sticker objects."""
        return self.retort.load(
            await self.session.call_method(
                "getForumTopicIconStickers", GetForumTopicIconStickers()
            ),
            list[Sticker],
        )

    async def create_forum_topic(
        self,
        chat_id: int | str,
        name: str,
        icon_color: int | None = None,
        icon_custom_emoji_id: str | None = None,
    ) -> ForumTopic:
        """Use this method to create a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns information about the created topic as a ForumTopic object."""
        return self.retort.load(
            await self.session.call_method(
                "createForumTopic",
                CreateForumTopic(chat_id, name, icon_color, icon_custom_emoji_id),
            ),
            ForumTopic,
        )

    async def edit_forum_topic(
        self,
        chat_id: int | str,
        message_thread_id: int,
        name: str | None = None,
        icon_custom_emoji_id: str | None = None,
    ) -> bool:
        """Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "editForumTopic",
                EditForumTopic(chat_id, message_thread_id, name, icon_custom_emoji_id),
            ),
            bool,
        )

    async def close_forum_topic(
        self, chat_id: int | str, message_thread_id: int
    ) -> bool:
        """Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "closeForumTopic", CloseForumTopic(chat_id, message_thread_id)
            ),
            bool,
        )

    async def reopen_forum_topic(
        self, chat_id: int | str, message_thread_id: int
    ) -> bool:
        """Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "reopenForumTopic", ReopenForumTopic(chat_id, message_thread_id)
            ),
            bool,
        )

    async def delete_forum_topic(
        self, chat_id: int | str, message_thread_id: int
    ) -> bool:
        """Use this method to delete a forum topic along with all its messages in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_delete_messages administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "deleteForumTopic", DeleteForumTopic(chat_id, message_thread_id)
            ),
            bool,
        )

    async def unpin_all_forum_topic_messages(
        self, chat_id: int | str, message_thread_id: int
    ) -> bool:
        """Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "unpinAllForumTopicMessages",
                UnpinAllForumTopicMessages(chat_id, message_thread_id),
            ),
            bool,
        )

    async def edit_general_forum_topic(self, chat_id: int | str, name: str) -> bool:
        """Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "editGeneralForumTopic", EditGeneralForumTopic(chat_id, name)
            ),
            bool,
        )

    async def close_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to close an open 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "closeGeneralForumTopic", CloseGeneralForumTopic(chat_id)
            ),
            bool,
        )

    async def reopen_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically unhidden if it was hidden. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "reopenGeneralForumTopic", ReopenGeneralForumTopic(chat_id)
            ),
            bool,
        )

    async def hide_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically closed if it was open. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "hideGeneralForumTopic", HideGeneralForumTopic(chat_id)
            ),
            bool,
        )

    async def unhide_general_forum_topic(self, chat_id: int | str) -> bool:
        """Use this method to unhide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "unhideGeneralForumTopic", UnhideGeneralForumTopic(chat_id)
            ),
            bool,
        )

    async def unpin_all_general_forum_topic_messages(self, chat_id: int | str) -> bool:
        """Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "unpinAllGeneralForumTopicMessages",
                UnpinAllGeneralForumTopicMessages(chat_id),
            ),
            bool,
        )

    async def answer_callback_query(
        self,
        callback_query_id: str,
        text: str | None = None,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: int | None = None,
    ) -> bool:
        """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "answerCallbackQuery",
                AnswerCallbackQuery(
                    callback_query_id, text, show_alert, url, cache_time
                ),
            ),
            bool,
        )

    async def set_my_commands(
        self,
        commands: list[BotCommand],
        scope: BotCommandScope | None = None,
        language_code: str | None = None,
    ) -> bool:
        """Use this method to change the list of the bot's commands. See this manual for more details about bot commands. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setMyCommands", SetMyCommands(commands, scope, language_code)
            ),
            bool,
        )

    async def delete_my_commands(
        self, scope: BotCommandScope | None = None, language_code: str | None = None
    ) -> bool:
        """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "deleteMyCommands", DeleteMyCommands(scope, language_code)
            ),
            bool,
        )

    async def get_my_commands(
        self, scope: BotCommandScope | None = None, language_code: str | None = None
    ) -> list[BotCommand]:
        """Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned."""
        return self.retort.load(
            await self.session.call_method(
                "getMyCommands", GetMyCommands(scope, language_code)
            ),
            list[BotCommand],
        )

    async def set_my_name(
        self, name: str | None = None, language_code: str | None = None
    ) -> bool:
        """Use this method to change the bot's name. Returns True on success."""
        return self.retort.load(
            await self.session.call_method("setMyName", SetMyName(name, language_code)),
            bool,
        )

    async def get_my_name(self, language_code: str | None = None) -> BotName:
        """Use this method to get the current bot name for the given user language. Returns BotName on success."""
        return self.retort.load(
            await self.session.call_method("getMyName", GetMyName(language_code)),
            BotName,
        )

    async def set_my_description(
        self, description: str | None = None, language_code: str | None = None
    ) -> bool:
        """Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setMyDescription", SetMyDescription(description, language_code)
            ),
            bool,
        )

    async def get_my_description(
        self, language_code: str | None = None
    ) -> BotDescription:
        """Use this method to get the current bot description for the given user language. Returns BotDescription on success."""
        return self.retort.load(
            await self.session.call_method(
                "getMyDescription", GetMyDescription(language_code)
            ),
            BotDescription,
        )

    async def set_my_short_description(
        self, short_description: str | None = None, language_code: str | None = None
    ) -> bool:
        """Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setMyShortDescription",
                SetMyShortDescription(short_description, language_code),
            ),
            bool,
        )

    async def get_my_short_description(
        self, language_code: str | None = None
    ) -> BotShortDescription:
        """Use this method to get the current bot short description for the given user language. Returns BotShortDescription on success."""
        return self.retort.load(
            await self.session.call_method(
                "getMyShortDescription", GetMyShortDescription(language_code)
            ),
            BotShortDescription,
        )

    async def set_chat_menu_button(
        self, chat_id: int | None = None, menu_button: MenuButton | None = None
    ) -> bool:
        """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setChatMenuButton", SetChatMenuButton(chat_id, menu_button)
            ),
            bool,
        )

    async def get_chat_menu_button(self, chat_id: int | None = None) -> MenuButton:
        """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success."""
        return self.retort.load(
            await self.session.call_method(
                "getChatMenuButton", GetChatMenuButton(chat_id)
            ),
            MenuButton,
        )

    async def set_my_default_administrator_rights(
        self,
        rights: ChatAdministratorRights | None = None,
        for_channels: bool | None = None,
    ) -> bool:
        """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setMyDefaultAdministratorRights",
                SetMyDefaultAdministratorRights(rights, for_channels),
            ),
            bool,
        )

    async def get_my_default_administrator_rights(
        self, for_channels: bool | None = None
    ) -> ChatAdministratorRights:
        """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success."""
        return self.retort.load(
            await self.session.call_method(
                "getMyDefaultAdministratorRights",
                GetMyDefaultAdministratorRights(for_channels),
            ),
            ChatAdministratorRights,
        )

    async def edit_message_text(
        self,
        text: str,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        disable_web_page_preview: bool | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "editMessageText",
                EditMessageText(
                    text,
                    chat_id,
                    message_id,
                    inline_message_id,
                    parse_mode,
                    entities,
                    disable_web_page_preview,
                    reply_markup,
                ),
            ),
            Message | bool,
        )

    async def edit_message_caption(
        self,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "editMessageCaption",
                EditMessageCaption(
                    chat_id,
                    message_id,
                    inline_message_id,
                    caption,
                    parse_mode,
                    caption_entities,
                    reply_markup,
                ),
            ),
            Message | bool,
        )

    async def edit_message_media(
        self,
        media: InputMedia,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "editMessageMedia",
                EditMessageMedia(
                    media, chat_id, message_id, inline_message_id, reply_markup
                ),
            ),
            Message | bool,
        )

    async def edit_message_live_location(
        self,
        latitude: float,
        longitude: float,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        horizontal_accuracy: float | None = None,
        heading: int | None = None,
        proximity_alert_radius: int | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "editMessageLiveLocation",
                EditMessageLiveLocation(
                    latitude,
                    longitude,
                    chat_id,
                    message_id,
                    inline_message_id,
                    horizontal_accuracy,
                    heading,
                    proximity_alert_radius,
                    reply_markup,
                ),
            ),
            Message | bool,
        )

    async def stop_message_live_location(
        self,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "stopMessageLiveLocation",
                StopMessageLiveLocation(
                    chat_id, message_id, inline_message_id, reply_markup
                ),
            ),
            Message | bool,
        )

    async def edit_message_reply_markup(
        self,
        chat_id: int | str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message | bool:
        """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "editMessageReplyMarkup",
                EditMessageReplyMarkup(
                    chat_id, message_id, inline_message_id, reply_markup
                ),
            ),
            Message | bool,
        )

    async def stop_poll(
        self,
        chat_id: int | str,
        message_id: int,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Poll:
        """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned."""
        return self.retort.load(
            await self.session.call_method(
                "stopPoll", StopPoll(chat_id, message_id, reply_markup)
            ),
            Poll,
        )

    async def delete_message(self, chat_id: int | str, message_id: int) -> bool:
        """Use this method to delete a message, including service messages, with the following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
        Returns True on success.
        """
        return self.retort.load(
            await self.session.call_method(
                "deleteMessage", DeleteMessage(chat_id, message_id)
            ),
            bool,
        )

    async def send_sticker(
        self,
        chat_id: int | str,
        sticker: IOBase | str,
        message_thread_id: int | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        """Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendSticker",
                SendSticker(
                    chat_id,
                    sticker,
                    message_thread_id,
                    emoji,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def get_sticker_set(self, name: str) -> StickerSet:
        """Use this method to get a sticker set. On success, a StickerSet object is returned."""
        return self.retort.load(
            await self.session.call_method("getStickerSet", GetStickerSet(name)),
            StickerSet,
        )

    async def get_custom_emoji_stickers(
        self, custom_emoji_ids: list[str]
    ) -> list[Sticker]:
        """Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects."""
        return self.retort.load(
            await self.session.call_method(
                "getCustomEmojiStickers", GetCustomEmojiStickers(custom_emoji_ids)
            ),
            list[Sticker],
        )

    async def upload_sticker_file(
        self, user_id: int, sticker: IOBase, sticker_format: str
    ) -> File:
        """Use this method to upload a file with a sticker for later use in the createNewStickerSet and addStickerToSet methods (the file can be used multiple times). Returns the uploaded File on success."""
        return self.retort.load(
            await self.session.call_method(
                "uploadStickerFile", UploadStickerFile(user_id, sticker, sticker_format)
            ),
            File,
        )

    async def create_new_sticker_set(
        self,
        user_id: int,
        name: str,
        title: str,
        stickers: list[InputSticker],
        sticker_format: str,
        sticker_type: str | None = None,
        needs_repainting: bool | None = None,
    ) -> bool:
        """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "createNewStickerSet",
                CreateNewStickerSet(
                    user_id,
                    name,
                    title,
                    stickers,
                    sticker_format,
                    sticker_type,
                    needs_repainting,
                ),
            ),
            bool,
        )

    async def add_sticker_to_set(
        self, user_id: int, name: str, sticker: InputSticker
    ) -> bool:
        """Use this method to add a new sticker to a set created by the bot. The format of the added sticker must match the format of the other stickers in the set. Emoji sticker sets can have up to 200 stickers. Animated and video sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "addStickerToSet", AddStickerToSet(user_id, name, sticker)
            ),
            bool,
        )

    async def set_sticker_position_in_set(self, sticker: str, position: int) -> bool:
        """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setStickerPositionInSet", SetStickerPositionInSet(sticker, position)
            ),
            bool,
        )

    async def delete_sticker_from_set(self, sticker: str) -> bool:
        """Use this method to delete a sticker from a set created by the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "deleteStickerFromSet", DeleteStickerFromSet(sticker)
            ),
            bool,
        )

    async def set_sticker_emoji_list(self, sticker: str, emoji_list: list[str]) -> bool:
        """Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setStickerEmojiList", SetStickerEmojiList(sticker, emoji_list)
            ),
            bool,
        )

    async def set_sticker_keywords(
        self, sticker: str, keywords: list[str] | None = None
    ) -> bool:
        """Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setStickerKeywords", SetStickerKeywords(sticker, keywords)
            ),
            bool,
        )

    async def set_sticker_mask_position(
        self, sticker: str, mask_position: MaskPosition | None = None
    ) -> bool:
        """Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setStickerMaskPosition", SetStickerMaskPosition(sticker, mask_position)
            ),
            bool,
        )

    async def set_sticker_set_title(self, name: str, title: str) -> bool:
        """Use this method to set the title of a created sticker set. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setStickerSetTitle", SetStickerSetTitle(name, title)
            ),
            bool,
        )

    async def set_sticker_set_thumbnail(
        self, name: str, user_id: int, thumbnail: IOBase | str | None = None
    ) -> bool:
        """Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setStickerSetThumbnail",
                SetStickerSetThumbnail(name, user_id, thumbnail),
            ),
            bool,
        )

    async def set_custom_emoji_sticker_set_thumbnail(
        self, name: str, custom_emoji_id: str | None = None
    ) -> bool:
        """Use this method to set the thumbnail of a custom emoji sticker set. Returns True on success."""
        return self.retort.load(
            await self.session.call_method(
                "setCustomEmojiStickerSetThumbnail",
                SetCustomEmojiStickerSetThumbnail(name, custom_emoji_id),
            ),
            bool,
        )

    async def delete_sticker_set(self, name: str) -> bool:
        """Use this method to delete a sticker set that was created by the bot. Returns True on success."""
        return self.retort.load(
            await self.session.call_method("deleteStickerSet", DeleteStickerSet(name)),
            bool,
        )

    async def answer_inline_query(
        self,
        inline_query_id: str,
        results: list[InlineQueryResult],
        cache_time: int | None = None,
        is_personal: bool | None = None,
        next_offset: str | None = None,
        button: InlineQueryResultsButton | None = None,
    ) -> bool:
        """Use this method to send answers to an inline query. On success, True is returned.
        No more than 50 results per query are allowed.
        """
        return self.retort.load(
            await self.session.call_method(
                "answerInlineQuery",
                AnswerInlineQuery(
                    inline_query_id,
                    results,
                    cache_time,
                    is_personal,
                    next_offset,
                    button,
                ),
            ),
            bool,
        )

    async def answer_web_app_query(
        self, web_app_query_id: str, result: InlineQueryResult
    ) -> SentWebAppMessage:
        """Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned."""
        return self.retort.load(
            await self.session.call_method(
                "answerWebAppQuery", AnswerWebAppQuery(web_app_query_id, result)
            ),
            SentWebAppMessage,
        )

    async def send_invoice(
        self,
        chat_id: int | str,
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: list[LabeledPrice],
        message_thread_id: int | None = None,
        max_tip_amount: int | None = None,
        suggested_tip_amounts: list[int] | None = None,
        start_parameter: str | None = None,
        provider_data: str | None = None,
        photo_url: str | None = None,
        photo_size: int | None = None,
        photo_width: int | None = None,
        photo_height: int | None = None,
        need_name: bool | None = None,
        need_phone_number: bool | None = None,
        need_email: bool | None = None,
        need_shipping_address: bool | None = None,
        send_phone_number_to_provider: bool | None = None,
        send_email_to_provider: bool | None = None,
        is_flexible: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message:
        """Use this method to send invoices. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendInvoice",
                SendInvoice(
                    chat_id,
                    title,
                    description,
                    payload,
                    provider_token,
                    currency,
                    prices,
                    message_thread_id,
                    max_tip_amount,
                    suggested_tip_amounts,
                    start_parameter,
                    provider_data,
                    photo_url,
                    photo_size,
                    photo_width,
                    photo_height,
                    need_name,
                    need_phone_number,
                    need_email,
                    need_shipping_address,
                    send_phone_number_to_provider,
                    send_email_to_provider,
                    is_flexible,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def create_invoice_link(
        self,
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: list[LabeledPrice],
        max_tip_amount: int | None = None,
        suggested_tip_amounts: list[int] | None = None,
        provider_data: str | None = None,
        photo_url: str | None = None,
        photo_size: int | None = None,
        photo_width: int | None = None,
        photo_height: int | None = None,
        need_name: bool | None = None,
        need_phone_number: bool | None = None,
        need_email: bool | None = None,
        need_shipping_address: bool | None = None,
        send_phone_number_to_provider: bool | None = None,
        send_email_to_provider: bool | None = None,
        is_flexible: bool | None = None,
    ) -> str:
        """Use this method to create a link for an invoice. Returns the created invoice link as String on success."""
        return self.retort.load(
            await self.session.call_method(
                "createInvoiceLink",
                CreateInvoiceLink(
                    title,
                    description,
                    payload,
                    provider_token,
                    currency,
                    prices,
                    max_tip_amount,
                    suggested_tip_amounts,
                    provider_data,
                    photo_url,
                    photo_size,
                    photo_width,
                    photo_height,
                    need_name,
                    need_phone_number,
                    need_email,
                    need_shipping_address,
                    send_phone_number_to_provider,
                    send_email_to_provider,
                    is_flexible,
                ),
            ),
            str,
        )

    async def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: list[ShippingOption] | None = None,
        error_message: str | None = None,
    ) -> bool:
        """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned."""
        return self.retort.load(
            await self.session.call_method(
                "answerShippingQuery",
                AnswerShippingQuery(
                    shipping_query_id, ok, shipping_options, error_message
                ),
            ),
            bool,
        )

    async def answer_pre_checkout_query(
        self, pre_checkout_query_id: str, ok: bool, error_message: str | None = None
    ) -> bool:
        """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent."""
        return self.retort.load(
            await self.session.call_method(
                "answerPreCheckoutQuery",
                AnswerPreCheckoutQuery(pre_checkout_query_id, ok, error_message),
            ),
            bool,
        )

    async def set_passport_data_errors(
        self, user_id: int, errors: list[PassportElementError]
    ) -> bool:
        """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success.
        Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.
        """
        return self.retort.load(
            await self.session.call_method(
                "setPassportDataErrors", SetPassportDataErrors(user_id, errors)
            ),
            bool,
        )

    async def send_game(
        self,
        chat_id: int,
        game_short_name: str,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> Message:
        """Use this method to send a game. On success, the sent Message is returned."""
        return self.retort.load(
            await self.session.call_method(
                "sendGame",
                SendGame(
                    chat_id,
                    game_short_name,
                    message_thread_id,
                    disable_notification,
                    protect_content,
                    reply_to_message_id,
                    allow_sending_without_reply,
                    reply_markup,
                ),
            ),
            Message,
        )

    async def set_game_score(
        self,
        user_id: int,
        score: int,
        force: bool | None = None,
        disable_edit_message: bool | None = None,
        chat_id: int | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
    ) -> Message | bool:
        """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False."""
        return self.retort.load(
            await self.session.call_method(
                "setGameScore",
                SetGameScore(
                    user_id,
                    score,
                    force,
                    disable_edit_message,
                    chat_id,
                    message_id,
                    inline_message_id,
                ),
            ),
            Message | bool,
        )

    async def get_game_high_scores(
        self,
        user_id: int,
        chat_id: int | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
    ) -> list[GameHighScore]:
        """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of GameHighScore objects."""
        return self.retort.load(
            await self.session.call_method(
                "getGameHighScores",
                GetGameHighScores(user_id, chat_id, message_id, inline_message_id),
            ),
            list[GameHighScore],
        )


__all__ = ["MethodsWrapper"]
