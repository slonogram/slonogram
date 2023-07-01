from typing import Optional, Awaitable

from ..schemas.chat import ParseMode, Message
from .group import CallsGroup


class ChatCallGroup(CallsGroup):
    def send_message(
        self,
        chat_id: int | str,
        text: Optional[str] = None,
        parse_mode: Optional[ParseMode] = None,
        reply_to: Optional[int] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> Awaitable[Message]:
        return self._call(
            Message,
            "sendMessage",
            {"chat_id": chat_id},
            (
                ("text", text),
                ("parse_mode", parse_mode),
                ("reply_to_message_id", reply_to),
                ("disable_web_page_preview", disable_web_page_preview),
                ("disable_notification", disable_notification),
                ("protect_content", protect_content),
                (
                    "allow_sending_without_reply",
                    allow_sending_without_reply,
                ),
            ),
        )
