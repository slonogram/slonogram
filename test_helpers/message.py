from slonogram.schemas import Message, Chat


CHAT_MOCK = Chat(id=1337, type="group", title="Nero's chat")
MESSAGE_MOCK = Message(message_id=1, date=1702279064, chat=CHAT_MOCK)

__all__ = [
    "CHAT_MOCK",
    "MESSAGE_MOCK",
]
