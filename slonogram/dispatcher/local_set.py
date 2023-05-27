from typing import (
    Optional,
    List,
    Self,
    Generic,
    TypeVar,
    Callable,
)

from ..schemas.updates import UpdateType
from ..schemas.chat import Message

from .handler import Handler, HandlerFn, FilterFn

T = TypeVar("T")


class EntryScope(Generic[T]):
    def __init__(
        self,
        update_type: UpdateType,
        append_fn: Callable[[Handler[T]], None],
    ) -> None:
        self._append_fn = append_fn
        self.update_type = update_type

    def when(
        self,
        filter_: FilterFn[T],
    ) -> Callable[[HandlerFn[T]], None]:
        def when_inner(fn: HandlerFn[T]) -> None:
            self._append_fn(Handler(fn, filter_, self.update_type))

        return when_inner


class LocalSet:
    def __init__(self, name: Optional[str] = None) -> None:
        self._name = name
        self._handlers: List[Handler] = []
        self._sets: List[Self] = []

    def register_handler(self, handler: Handler) -> None:
        self._handlers.append(handler)

    @property
    def message(self) -> EntryScope[Message]:
        return EntryScope(UpdateType.message, self.register_handler)

    @property
    def name(self) -> Optional[str]:
        return self._name


__all__ = ["LocalSet", "EntryScope"]
