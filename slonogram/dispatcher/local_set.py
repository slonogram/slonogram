from typing import Optional, List, Self, Generic, TypeVar, Callable, Any

from ..bot import Bot
from ..schemas.updates import UpdateType, Update
from ..schemas.chat import Message

from .handler import Handler, HandlerFn
from ..filtering import FilterFn

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
    def __init__(
        self,
        name: Optional[str] = None,
    ) -> None:
        self._name = name
        self._handlers: List[Handler[Any]] = []
        self._sets: List[Self] = []

    def register_handler(self, handler: Handler) -> None:
        self._handlers.append(handler)

    async def process_update(self, bot: Bot, update: Update) -> bool:
        for handler in self._handlers:
            data = update.message
            if data is None:
                raise NotImplementedError("TODO: non-message types")

            result = await handler.handle(bot, data)
            if result:
                return True
        for set_ in self._sets:
            if await set_.process_update(bot, update):
                return True
        return False

    @property
    def message(self) -> EntryScope[Message]:
        return EntryScope(UpdateType.message, self.register_handler)

    @property
    def name(self) -> Optional[str]:
        return self._name


__all__ = ["LocalSet", "EntryScope"]
