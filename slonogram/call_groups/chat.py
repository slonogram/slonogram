from typing import Optional, Awaitable, List

from ..schemas.chat import (
    ParseMode,
    Message,
    MessageEntity,
    InlineKeyboardMarkup,
)
from .group import CallsGroup


class ChatCallGroup(CallsGroup):
    def send_message(
        self,
        chat_id: int | str,
        text: Optional[str] = None,
        parse_mode: Optional[ParseMode] = None,
        reply_to: Optional[int] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> Awaitable[Message]:
        """
        Sends a message to chat
        :param chat_id: Chat's ID
        :param text: Text of message
        :param parse_mode: Parse-mode, can be `html` or `markdown`
        :param reply_to: Reply to message? Pass `ID` of message to reply
        :param entities: List of message's entities
        :param disable_web_page_preview: Disable preview?
        :param disable_notification: Disable notification?
        :param protect_content: Protect content?
        :param allow_sending_without_reply: Allow sending without reply?
        :return: Sent message on success
        """
        return self._call(
            Message,
            "sendMessage",
            {"chat_id": chat_id},
            (
                ("text", text),
                ("parse_mode", parse_mode),
                ("reply_to_message_id", reply_to),
                ("entities", entities),
                ("disable_web_page_preview", disable_web_page_preview),
                ("disable_notification", disable_notification),
                ("protect_content", protect_content),
                (
                    "allow_sending_without_reply",
                    allow_sending_without_reply,
                ),
            ),
        )

    def edit_message_text(
        self,
        text: str,
        chat_id: Optional[int | str] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Awaitable[Message]:
        """
        Edits message's text, pass `chat_id` with `message_id` or `inline_message_id`
        :param text: New text for the message
        :param chat_id: Chat's ID
        :param parse_mode: Parse-mode, can be `html` or `markdown`
        :param entities: List of message's entities
        :param disable_web_page_preview: Disable preview?
        :param reply_markup: New reply-markup
        :return: Edited message on success
        """

        if not chat_id and not message_id and not inline_message_id:
            raise ValueError(
                "Please, pass `chat_id` with `message_id` or `inline_message_id`"
            )

        return self._call(
            Message,
            "editMessageText",
            {"text": text},
            (
                ("chat_id", chat_id),
                ("message_id", message_id),
                ("inline_message_id", inline_message_id),
                ("parse_mode", parse_mode),
                ("entities", entities),
                ("disable_web_page_preview", disable_web_page_preview),
                ("reply_markup", reply_markup),
            ),
        )
