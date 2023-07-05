from enum import IntFlag, auto


class MessageSubtypes(IntFlag):
    SENT = auto()
    EDITED = auto()
