from typing import Awaitable, Optional, List  # noqa
import slonogram.schemas  # noqa
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps  # noqa


class ChatCallGroup:
    __slots__ = ("_session",)

    def __init__(self, session: ApiSession) -> None:
        self._session = session

    async def send_action(
        self,
        chat_id: int | str,
        action: str,
        message_thread_id: Optional[int] = None,
    ) -> bool:
        """
        Use this method when you need to tell the user that something is
        happening on the bot's side. The status is set for 5 seconds or
        less (when a message arrives from your bot, Telegram clients
        clear its typing status). Returns True on success. We only
        recommend using this method when a response from the bot will
        take a noticeable amount of time to arrive. for more:
        https://core.telegram.org/bots/api#sendchataction
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread; supergroups only
        :param action: Type of action to broadcast. Choose one,
                       depending on what the user is about to
                       receive: typing for text messages,
                       upload_photo for photos, record_video or
                       upload_video for videos, record_voice or
                       upload_voice for voice notes, upload_document
                       for general files, choose_sticker for
                       stickers, find_location for location data,
                       record_video_note or upload_video_note for
                       video notes.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "action": action}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        return await self._session.call_method(
            bool, "sendChatAction", params
        )

    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        message_thread_id: Optional[int] = None,
        parse_mode: Optional[slonogram.schemas.ParseMode] = None,
        entities: Optional[List[slonogram.schemas.MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            slonogram.schemas.InlineKeyboardMarkup
            | slonogram.schemas.ReplyKeyboardMarkup
            | slonogram.schemas.ReplyKeyboardRemove
            | slonogram.schemas.ForceReply
        ] = None,
    ) -> slonogram.schemas.Message:
        """
        Use this method to send text messages. On success, the sent
        Message is returned. for more:
        https://core.telegram.org/bots/api#sendmessage
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param text: Text of the message to be sent, 1-4096
                     characters after entities parsing
        :param parse_mode: Mode for parsing entities in the message
                           text. See formatting options for more
                           details.
        :param entities: A JSON-serialized list of special entities
                         that appear in message text, which can be
                         specified instead of parse_mode
        :param disable_web_page_preview: Disables link previews for
                                         links in this message
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "text": text}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if entities is not None:
            params["entities"] = dumps(self._session.retort.dump(entities))

        if disable_web_page_preview is not None:
            params["disable_web_page_preview"] = disable_web_page_preview

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = dumps(
                self._session.retort.dump(reply_markup)
            )

        return await self._session.call_method(
            slonogram.schemas.Message, "sendMessage", params
        )
