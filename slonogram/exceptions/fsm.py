from typing import TypeVar, Generic, Type, Any
from ..types.fsm import StorageScope

T = TypeVar("T")


class FailedToWrite(Generic[T], Exception):
    __slots__ = ("scope", "data", "message")

    def __init__(
        self,
        scope: StorageScope[Any],
        data: T,
        message: str,
    ) -> None:
        self.scope = scope
        self.data = data
        self.message = message

        super().__init__(f"failed to write to the FSM storage at {scope}: {message}")


class NoSuchEntry(Generic[T], Exception):
    __slots__ = ("scope", "type")

    def __init__(self, tp: Type[T], scope: StorageScope[Any]) -> None:
        self.scope = scope
        self.type = tp

        super().__init__(f"no such entry at {scope}")


class WrongType(Generic[T], Exception):
    __slots__ = ("scope", "type", "actual")

    def __init__(
        self,
        scope: StorageScope[Any],
        tp: Type[T],
        actual: Type[Any] | None = None,
    ) -> None:
        if actual is not None:
            super().__init__(
                f"wrong type of data supplied at {scope}: {tp}, while actual is {actual}"
            )
        else:
            super().__init__(f"wrong type of data supplied at {scope}: {tp}")

        self.scope = scope
        self.tp = tp
        self.actual = actual


__all__ = [
    "FailedToWrite",
    "WrongType",
    "NoSuchEntry",
]
