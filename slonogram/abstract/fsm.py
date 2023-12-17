from typing import Callable, Protocol, Type, TypeVar
from slonogram.types.fsm import StorageScope

T = TypeVar("T")
S = TypeVar("S")


class FSMStorage(Protocol):
    async def write(self, scope: StorageScope[S], value: T) -> None:
        """Write data to the `scope` scope. Overwrites scope if value already exists.

        :param scope: scope to write
        :param value: value to write

        :raises slonogram.exceptions.fsm.FailedToWrite[T]: if underlying implementation fail writing
        """

    async def read(
        self,
        scope: StorageScope[S],
        type: Type[T],
        *,
        init_with: Callable[[], T] | None = None,
    ) -> T:
        """Reads type `type` from the scope `scope`.

        :param scope: scope to read
        :param type: type to read
        :param init_with: initialize with the result of lazy computation if `scope` was not found

        :raises slonogram.exceptions.fsm.WrongType: if `scope` contains not the `type` type
        :raises slonogram.exceptions.fsm.NoSuchEntry: if there's no such `scope` and `init_with` is None
        """


def assert_compatible(tp: Type[FSMStorage]) -> None:
    _ = tp


__all__ = [
    "FSMEntry",
    "FSMStorage",
    "assert_compatible",
]
