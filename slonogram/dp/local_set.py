from __future__ import annotations
from typing import (
    Optional,
    List,
    TypeVar,
    Generic,
    Callable,
    TypeAlias,
    Iterable,
    Any,
)

from .handler import HandlerFn, Handler
from .middlewares import Middlewares

from ..filters.extended import always_true
from ..filters.types import FilterFn
from ..schemas.chat import Message

T = TypeVar("T")
D = TypeVar("D")
_OptFilterFn: TypeAlias = Optional[FilterFn[D, T]]
_RegisterRetDeco: TypeAlias = Callable[[HandlerFn[D, T]], Handler[D, T]]


class LocalSet(Generic[D]):
    def __init__(self, name: Optional[str]) -> None:
        self.name = name

        self._children: List[LocalSet] = []
        self._handlers = _Handlers[D]()
        self._middlewares = Middlewares[D, Any]()

    def include_set(self, set_: LocalSet) -> None:
        self._children.append(set_)

    def include_sets(self, sets: Iterable[LocalSet]) -> None:
        self._children.extend(sets)

    @property
    def on_message(self) -> MessageScope[D]:
        return MessageScope(self._handlers)


class _TakesHandlers(Generic[D]):
    def __init__(self, handlers: _Handlers[D]) -> None:
        self._handlers = handlers


class MessageScope(_TakesHandlers[D]):
    def _generic_register(
        self,
        append_to: List[Handler[D, Message]],
        filter_fn: _OptFilterFn[D, Message],
        prefer_bot_arg: bool,
    ) -> _RegisterRetDeco[D, Message]:
        u_filter_fn = filter_fn or always_true

        def _ret_deco(h_fn: HandlerFn[D, Message]) -> Handler[D, Message]:
            handler = Handler(prefer_bot_arg, h_fn, u_filter_fn)
            append_to.append(handler)
            return handler

        return _ret_deco

    # Can we somehow reduce this to smth like:
    # ```
    # sent = _register_fn('sent', 'message')
    # edited = _register_fn('edited', 'edited_message')
    # ```
    #
    # and satisfy `mypy`? I spent some time writing function `_register_fn`,
    # but looks like `mypy` isn't satisfied with that approach.
    def sent(
        self,
        filter_fn: _OptFilterFn[D, Message] = None,
        prefer_bot_arg: bool = True,
    ) -> _RegisterRetDeco[D, Message]:
        return self._generic_register(
            self._handlers.message, filter_fn, prefer_bot_arg
        )

    def edited(
        self,
        filter_fn: _OptFilterFn[D, Message] = None,
        prefer_bot_arg: bool = True,
    ) -> _RegisterRetDeco[D, Message]:
        return self._generic_register(
            self._handlers.edited_message, filter_fn, prefer_bot_arg
        )


class _Handlers(Generic[D]):
    __slots__ = "message", "edited_message"

    message: List[Handler[D, Message]]
    edited_message: List[Handler[D, Message]]

    def __init__(self) -> None:
        self.message = []
        self.edited_message = []
