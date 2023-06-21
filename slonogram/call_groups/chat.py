from typing import Optional, Awaitable

from ..schemas.chat import ParseMode, Message
from .group import CallsGroup


class ChatCallGroup(CallsGroup):
    def send_message(
        self,
        chat_id: int | str,
        text: Optional[str] = None,
        parse_mode: Optional[ParseMode] = None,
    ) -> Awaitable[Message]:
        return self._call(
            Message,
            "sendMessage",
            {"chat_id": chat_id},
            (("text", text), ("parse_mode", parse_mode)),
        )
