from __future__ import annotations
from typing import (
    Optional,
    List,
    TypeVar,
    Generic,
    Callable,
    TypeAlias,
    Any,
    Awaitable,
)

from .context import Context
from .handler import HandlerFn, Handler
from .middlewares import Middlewares

from ..exceptions.control_flow import SkipLocalSet, DontHandle
from ..filters.extended import always_true
from ..filters.types import FilterFn
from ..schemas.chat import Message
from ..schemas.updates import Update

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

    def include(self, *sets: LocalSet) -> None:
        self._children.extend(sets)

    @property
    def on_message(self) -> MessageScope[D]:
        return MessageScope(self._handlers)

    async def _process_message(
        self,
        ctx: Context[D, Message],
        handlers: List[Handler[D, Message]],
    ) -> bool:
        for handler in handlers:
            invoked = await handler.try_invoke(ctx)
            if invoked:
                return True

        return False

    async def _process_update(
        self,
        # if ctx.model is None this means that this set is root
        ctx: Context[D, Any],
        update: Update,
    ) -> bool:
        tg = ctx.inter.task_group
        middlewares = self._middlewares

        run_before = middlewares.run_before
        handlers = self._handlers

        call_fn: Callable[
            [Context[D, Any], List[Handler[D, Message]]], Awaitable[bool]
        ]
        provided_handlers: List[Handler[D, Any]]

        if update.message is not None:
            ctx.model = update.message
            call_fn = self._process_message
            provided_handlers = handlers.message
        elif update.edited_message is not None:
            ctx.model = update.edited_message
            call_fn = self._process_message
            provided_handlers = handlers.edited_message
        else:
            raise NotImplementedError

        ctx: Context[D, Any]  # type: ignore

        for before_ooo in run_before.out_of_order:
            tg.start_soon(before_ooo, ctx)

        # IDK how to reduce code size here,
        # Do we need it actually?
        try:
            for before_strict in run_before.strict:
                try:
                    await before_strict(ctx)
                except SkipLocalSet:
                    return False

            result = await call_fn(ctx, provided_handlers)
            ctx._patches.clear()
            if result:
                return True

            for child in self._children:
                processed = await child._process_update(ctx, update)
                if processed:
                    return True
        except SkipLocalSet:
            return False
        except DontHandle as e:
            if ctx.model is None:
                raise e
            return False
        finally:
            run_after = middlewares.run_after
            for after_ooo in run_after.out_of_order:
                tg.start_soon(after_ooo, ctx)
            for after_strict in run_after.strict:
                try:
                    await after_strict(ctx)
                except DontHandle as e:
                    if ctx.model is None:
                        raise e
                    return False
                except SkipLocalSet:
                    return False

            ctx._patches.clear()

        return False


class _TakesHandlers(Generic[D]):
    def __init__(self, handlers: _Handlers[D]) -> None:
        self._handlers = handlers


class MessageScope(_TakesHandlers[D]):
    # Also, `prefer_bot_arg` can be retrieved from the type hints
    # TODO: make this decorator less verbose
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
