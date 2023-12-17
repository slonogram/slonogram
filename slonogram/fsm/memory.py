from typing import TypeVar, Type, Any, Callable

from slonogram.exceptions.fsm import NoSuchEntry
from slonogram.abstract.fsm import assert_compatible
from slonogram.types.fsm import StorageScope


T = TypeVar("T")
S = TypeVar("S")


class MemoryStorage:
    """Basic and very primitive storage based on the `dict`.

    :param content: content of the storage
    """

    def __init__(
        self,
        content: dict[StorageScope[Any], Any] | None = None,
    ) -> None:
        self.content = content or {}

    async def write(self, scope: StorageScope[S], value: T) -> None:
        self.content[scope] = value

    async def read(
        self,
        scope: StorageScope[S],
        type: Type[T],
        *,
        init_with: Callable[[], T] | None = None,
    ) -> T:
        try:
            value = self.content[scope]
        except KeyError:
            if init_with is None:
                raise NoSuchEntry[T](type, scope)
            value = init_with()

        return value


assert_compatible(MemoryStorage)
