from enum import IntFlag, auto
from typing import TypeAlias


class EmptyFlags(IntFlag):
    EMPTY = auto()


class MessageFlags(IntFlag):
    SENT = auto()
    EDITED = auto()


EventFlags: TypeAlias = MessageFlags | EmptyFlags
