from dataclasses import dataclass
from typing import Optional, List, TypeVar, Generic, Callable

from .handler import HandlerFn, Handler

from ..filters.extended import always_true
from ..filters.types import FilterFn
from ..schemas.chat import Message

T = TypeVar("T")
D = TypeVar("D")


@dataclass(slots=True)
class _Handlers(Generic[D]):
    message: List[Handler[D, Message]]
    edited_message: List[Handler[D, Message]]


class _TakesRegisterFn(Generic[D, T]):
    def __init__(
        self, register_fn: Callable[[Handler[D, T]], None]
    ) -> None:
        self._register_fn = register_fn


class MessageScope(Generic[D], _TakesRegisterFn[D, Message]):
    def sent(
        self,
        filter_fn: Optional[FilterFn[D, Message]] = None,
        prefer_bot_arg: bool = True,
    ) -> Callable[[HandlerFn[D, Message]], None]:
        u_filter_fn: FilterFn[D, Message]
        if filter_fn is None:
            u_filter_fn = always_true
        else:
            u_filter_fn = filter_fn

        def sent_inner(fn: HandlerFn[D, Message]) -> None:
            self._register_fn(
                Handler(
                    prefer_bot_arg,
                    fn,
                    u_filter_fn,
                )
            )

        return sent_inner


class LocalSet(Generic[D]):
    def __init__(self, name: Optional[str]) -> None:
        self.name = name
        self._handlers = _Handlers[D]([], [])

    @property
    def on_message(self) -> MessageScope[D]:
        return MessageScope(self._handlers.message.append)
