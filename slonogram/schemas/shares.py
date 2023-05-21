from dataclasses import dataclass


@dataclass
class ChatShared:
    request_id: int
    chat_id: int


@dataclass
class UserShared:
    request_id: int
    user_id: int
