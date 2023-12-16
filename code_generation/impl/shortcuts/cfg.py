from code_generation.library.type_hint import Ref, TypeHint
from code_generation.library.type_hint.ref_sources import Source, SCHEMAS

from dataclasses import dataclass

ABSTRACT_CONTEXT_SRC = Source("slonogram.abstract.context")
ABSTRACT_CONTEXT = Ref(ABSTRACT_CONTEXT_SRC, "AbstractContext")


@dataclass
class MethodRef:
    self_type: TypeHint
    alias_to: str
    replace_field_value: dict[str, str]


_WITH_CHAT = {"chat_id": "self.model.chat.id"}
M_MESSAGE = Ref(SCHEMAS, "Message")
M_CALLBACK = Ref(SCHEMAS, "CallbackQuery")


def _message_ref(
    method_name: str,
    add: dict[str, str] | None = None,
) -> MethodRef:
    d = {**_WITH_CHAT, **(add or {})}
    return MethodRef(ABSTRACT_CONTEXT[M_MESSAGE], method_name, d)


METHOD_CALLS = {
    "send_photo": _message_ref("sendPhoto"),
    "send_audio": _message_ref("sendAudio"),
    "send_document": _message_ref("sendDocument"),
    "send_video": _message_ref("sendVideo"),
    "send_animation": _message_ref("sendAnimation"),
    "send_voice": _message_ref("sendVoice"),
    "send_video_note": _message_ref("sendVideoNote"),
    "send_media_group": _message_ref("sendMediaGroup"),
    "send_location": _message_ref("sendLocation"),
    "send_venue": _message_ref("sendVenue"),
    "send_contact": _message_ref("sendContact"),
    "send_poll": _message_ref("sendPoll"),
    "send_dice": _message_ref("sendDice"),
    "send_action": _message_ref("sendChatAction"),
    "reply": _message_ref(
        "sendMessage", {"reply_to_message_id": "self.model.message_id"}
    ),
}
