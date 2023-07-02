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
from ..handling.handler import HandlerFn, Handler
from ..handling.middlewares import Middlewares

from ..exceptions.control_flow import SkipLocalSet, DontHandle
from ..filters.types import FilterFn
from ..schemas import Message, Update

T = TypeVar("T")
D = TypeVar("D")
_OptFilterFn: TypeAlias = Optional[FilterFn[D, T]]
_RegisterRetDeco: TypeAlias = Callable[[HandlerFn[D, T]], Handler[D, T]]


class LocalSet(Generic[D]):
    def __init__(
        self,
        name: Optional[str] = None,
        filter_: Optional[FilterFn[D, Any]] = None,
    ) -> None:
        self.name = name

        self._children: List[LocalSet] = []
        self._handlers = _Handlers[D]()
        self._middlewares = Middlewares[D, Any]()
        self.filter_ = filter_

    def include(self, *sets: LocalSet) -> None:
        self._children.extend(sets)

    @property
    def on_message(self) -> MessageScope[D]:
        return MessageScope(self._handlers)

    async def feed_update(
        self, ctx: Context[D, T], update: Update
    ) -> bool:
        raise NotImplementedError

    async def _process_ctx(
        self,
        ctx: Context[D, T],
        handlers: List[Handler[D, T]],
    ) -> bool:
        filter_ = self.filter_
        if filter_ is not None and not await filter_(ctx):
            return False

        check_pad = ctx.pad.create_child()
        ctx.pad = check_pad

        for handler in handlers:
            invoked = await handler.try_invoke(ctx)
            check_pad.clear()
            if invoked:
                return True

        return False

    async def _process_update(
        self,
        ctx: Context[D, Any],
        update: Update,
    ) -> bool:
        tg = ctx.inter.task_group
        middlewares = self._middlewares
        # if ctx.model is None this means that this set is root
        is_root = ctx.model is None

        run_before = middlewares.run_before
        handlers = self._handlers

        call_fn: Callable[
            [Context[D, Any], List[Handler[D, Any]]], Awaitable[bool]
        ] = self._process_ctx
        provided_handlers: List[Handler[D, Any]]

        if update.message is not None:
            ctx.model = update.message
            provided_handlers = handlers.message
        elif update.edited_message is not None:
            ctx.model = update.edited_message
            provided_handlers = handlers.edited_message
        else:
            raise NotImplementedError

        ctx: Context[D, Any]  # type: ignore

        for before_ooo in run_before.out_of_order:
            tg.start_soon(before_ooo, ctx)

        # IDK how to reduce code size here,
        # Do we need it actually?
        cur_pad = ctx.pad
        try:
            for before_strict in run_before.strict:
                try:
                    await before_strict(ctx)
                except SkipLocalSet:
                    return False

            result = await call_fn(ctx, provided_handlers)
            if result:
                return True

            for child in self._children:
                ctx.pad = cur_pad.create_child()
                processed = await child._process_update(ctx, update)
                if processed:
                    return True

        except SkipLocalSet:
            return False
        except DontHandle as e:
            if is_root:
                raise e
            return False
        finally:
            ctx.pad = cur_pad
            run_after = middlewares.run_after
            for after_ooo in run_after.out_of_order:
                tg.start_soon(after_ooo, ctx)
            for after_strict in run_after.strict:
                try:
                    await after_strict(ctx)
                except DontHandle as e:
                    if is_root:
                        raise e
                    return False
                except SkipLocalSet:
                    return False

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
        def _ret_deco(h_fn: HandlerFn[D, Message]) -> Handler[D, Message]:
            handler = Handler(prefer_bot_arg, h_fn, filter_fn)
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
