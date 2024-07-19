from enum import StrEnum, auto


class Interest(StrEnum):
    MESSAGE = auto()
    CALLBACK_QUERY = auto()
    INLINE_QUERY = auto()


__all__ = ["Interest"]


