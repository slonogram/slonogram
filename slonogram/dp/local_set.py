from dataclasses import dataclass
from typing import Optional, List, TypeVar, Generic, Callable

from .handler import HandlerFn, Handler

from ..filters.extended import always_true
from ..filters.types import FilterFn
from ..schemas.chat import Message

T = TypeVar("T")


@dataclass(slots=True)
class _Handlers:
    message: List[Handler[Message]]
    edited_message: List[Handler[Message]]


class _TakesRegisterFn(Generic[T]):
    def __init__(self, register_fn: Callable[[Handler[T]], None]) -> None:
        self._register_fn = register_fn


class MessageScope(_TakesRegisterFn[Message]):
    def sent(
        self,
        filter_fn: Optional[FilterFn[Message]] = None,
        prefer_bot_arg: bool = True,
    ) -> Callable[[HandlerFn[Message]], None]:
        u_filter_fn: FilterFn[Message]
        if filter_fn is None:
            u_filter_fn = always_true
        else:
            u_filter_fn = filter_fn

        def sent_inner(fn: HandlerFn[Message]) -> None:
            self._register_fn(
                Handler(
                    prefer_bot_arg,
                    fn,
                    u_filter_fn,
                )
            )

        return sent_inner


class LocalSet:
    def __init__(self, name: Optional[str]) -> None:
        self.name = name
        self._handlers = _Handlers([], [])

    @property
    def on_message(self) -> MessageScope:
        return MessageScope(self._handlers.message.append)
