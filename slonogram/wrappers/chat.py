from typing import Optional, Callable, Dict, Any

from ..protocols.session import Session
from ..schemas.chat import Message, ParseMode, MessageId
from ..schemas.message_entity import MessageEntity

from ..utils.dict import set_if_not_none


class ChatApiWrapper:
    def __init__(
        self, json_dumper: Callable[[Any], str], session: Session
    ) -> None:
        self._session = session
        self._json_dumper = json_dumper

    async def send_message(
        self,
        chat_id: int | str,
        text: Optional[str] = None,
        thread_id: Optional[int] = None,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[MessageEntity] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[MessageId] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> Message:
        args: Dict[str, Any] = {"chat_id": chat_id}
        set_if_not_none(
            args,
            (
                ("message_thread_id", thread_id),
                ("text", text),
                ("parse_mode", parse_mode),
                ("disable_web_page_preview", disable_web_page_preview),
                ("disable_notification", disable_notification),
                ("protect_content", protect_content),
                ("reply_to_message_id", reply_to),
                (
                    "allow_sending_without_reply",
                    allow_sending_without_reply,
                ),
            ),
        )

        if entities is not None:
            args["entities"] = self._json_dumper(entities)

        result = await self._session.raw_method(
            Message, "sendMessage", args
        )

        return result.unwrap_data()
