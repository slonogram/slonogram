from __future__ import annotations
from typing import Optional, Awaitable, List

from ..schemas import (
    ParseMode,
    Message,
    MessageEntity,
    InlineKeyboardMarkup,
    ChatAction,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
)
from .group import CallsGroup, UseRetort


class ChatCallGroup(CallsGroup):
    def send_action(
        self,
        chat_id: int | str,
        action: ChatAction,
        message_thread_id: Optional[int] = None,
    ) -> Awaitable[bool]:
        return self._call(
            bool,
            "sendChatAction",
            {"chat_id": chat_id, "action": action},
            (("message_thread_id", message_thread_id),),
        )

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
        reply_markup: Optional[
            InlineKeyboardMarkup
            | ReplyKeyboardMarkup
            | ReplyKeyboardRemove
            | ForceReply
        ] = None,
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
                UseRetort("reply_markup", reply_markup),
            ),
        )

    def forward_message(
        self,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
    ) -> Awaitable[Message]:
        """
        Use this method to forward messages of any kind
        Service messages can't be forwarded.
        On success, the sent `Message` is returned.

        :param chat_id: Chat's ID
        :param from_chat_id: Identifier for the chat where the original
                             message was sent
        :param message_id: Message identifier in the chat specified in
                           `from_chat_id`
        :param message_thread_id: Identifier for the target message thread
                                  (topic) of the forum
        :param disable_notification: Send the message silently?
        :param protect_content: Protects the contents of the forwarded message
                                from forwarding and saving
        """

        return self._call(
            Message,
            "forwardMessage",
            {
                "chat_id": chat_id,
                "from_chat_id": from_chat_id,
                "message_id": message_id,
            },
            (
                ("message_thread_id", message_thread_id),
                ("disable_notification", disable_notification),
                ("protect_content", protect_content),
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
        Edits message's text.
        Pass `chat_id` with `message_id` or `inline_message_id`

        :param text: New text for the message
        :param chat_id: Chat's ID
        :param parse_mode: Parse-mode, can be `html` or `markdown`
        :param entities: List of message's entities
        :param disable_web_page_preview: Disable preview?
        :param reply_markup: New reply-markup
        :return: Edited message on success
        """
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
