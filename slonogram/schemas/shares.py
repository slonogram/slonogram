from dataclasses import dataclass


@dataclass(slots=True)
class ChatShared:
    request_id: int
    chat_id: int


@dataclass(slots=True)
class UserShared:
    request_id: int
    user_id: int


__all__ = ["ChatShared", "UserShared"]
