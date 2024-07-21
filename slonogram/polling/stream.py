from __future__ import annotations

import typing as t
import functools as ft

from anyio import create_task_group

from sena.handling.continue_ import continue_

from ..schemas.update import Update
from ..handling.handler import HandlerFn

from ..utils.omit import Omittable, OMIT
from ..types.stash import Stash
from ..types.ctx import Ctx

P = t.ParamSpec("P")
CtxFactory: t.TypeAlias = t.Callable[[Update], Ctx[Update]]
I = t.TypeVar("I", Update, tuple[CtxFactory, Update])

class Stream(t.Generic[I]):
    __slots__ = ('iterator', )

    iterator: t.AsyncIterator[I]

    def __init__(self, iterator: t.AsyncIterator[I]) -> None:
        self.iterator = iterator

    @staticmethod
    def lift(f: t.Callable[P, t.AsyncIterator[I]]) -> t.Callable[P, Stream[I]]:
        @ft.wraps(f)
        def inner(*args: P.args, **kwargs: P.kwargs) -> Stream[I]:
            return Stream(f(*args, **kwargs))

        return inner

    def __aiter__(self) -> t.AsyncIterator[I]:
        return self.iterator

    @t.overload
    def __anext__(self: Stream[Update]) -> t.Awaitable[Update]:
        ...

    @t.overload
    def __anext__(self: Stream[tuple[CtxFactory, Update]]) -> t.Awaitable[tuple[CtxFactory, Update]]:
        ...

    def __anext__(self) -> t.Awaitable[t.Any]:
        return self.iterator.__anext__()

    @t.overload
    async def feed_to(
        self: Stream[tuple[CtxFactory, Update]],
        to: HandlerFn[Update],
        *,
        ctx_factory: Omittable[CtxFactory] = OMIT,
    ) -> None:
        ...

    @t.overload
    async def feed_to(
        self,
        to: HandlerFn[Update],
        *,
        ctx_factory: CtxFactory,
    ) -> None:
        ...

    async def feed_to(
        self,
        to: HandlerFn[Update],
        *,
        ctx_factory: Omittable[CtxFactory] = OMIT,
    ) -> None:
        async with create_task_group() as tg:
            async for item in self.iterator:
                _ctx_factory: CtxFactory
                event: Update

                if isinstance(item, tuple):
                    _ctx_factory, event = item
                    if ctx_factory is not OMIT:
                        _ctx_factory = t.cast(CtxFactory, ctx_factory)
                elif ctx_factory is OMIT:
                    raise ValueError(
                        "You must provide a `ctx_factory` to be able to create the context",
                    )
                else:
                    _ctx_factory = t.cast(CtxFactory, ctx_factory)
                    event = item

                ctx = _ctx_factory(event)
                tg.start_soon(to, ctx, continue_)


__all__ = ["Stream"]


