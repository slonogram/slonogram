from __future__ import annotations

import dataclasses as dtc
import typing as t

from ..utils.altering import alter1, Alterer1
from ..utils.omit import OMIT, Omittable
from ..types.ctx import Ctx

from ..schemas.callback_query import CallbackQuery
from ..schemas.message import Message
from ..schemas.update import Update

from .handler import (
    Handler,
    HandlerFn,
    Endpoint,
    ControlFlow,
)

D = t.TypeVar("D")
_Handlers: t.TypeAlias = tuple[Handler[D], ...]
_HAlterer: t.TypeAlias = Alterer1[_Handlers[D]]

@dtc.dataclass(slots=True)
class Slots:
    message: _Handlers[Message] = ()
    callback_query: _Handlers[CallbackQuery] = ()

    def alter(
        self,
        message: Omittable[_HAlterer[Message]] = OMIT,
        callback_query: Omittable[_HAlterer[CallbackQuery]] = OMIT,
    ) -> Slots:
        return Slots(
            message=alter1(message, self.message),
            callback_query=alter1(callback_query, self.callback_query)
        )


class DispatcherFn(HandlerFn[Update]):
    __slots__ = ('slots', )

    def __init__(self, slots: Slots) -> None:
        self.slots = slots

    def alter(
        self,
        slots: Omittable[Alterer1[Slots]] = OMIT,
    ) -> DispatcherFn:
        return DispatcherFn(slots=alter1(slots, self.slots))

    async def _feed(
        self,
        req: Ctx[D],
        next: Endpoint[D],
        handlers: _Handlers[D],
    ) -> ControlFlow[D]:
        raise NotImplementedError

    async def _feed_untyped(
        self,
        req: Ctx[D],
        next: Endpoint[Update],
        handlers: _Handlers[D],
        kind: str,
    ) -> ControlFlow[Update]:
        raise NotImplementedError  # mypy kinda sucks

    def __repr__(self) -> str:
        return f"DispatcherFn(slots={self.slots!r})"

    def __call__(self, req: Ctx[Update], next: Endpoint[Update]) -> t.Awaitable[ControlFlow[Update]]:
        upd = req.data
        slots = self.slots

        if upd.message is not None:
            return self._feed_untyped(
                req.with_data(upd.message),
                next,
                slots.message,
                'message',
            )
        elif upd.callback_query is not None:
            raise NotImplementedError

        raise NotImplementedError
    

__all__ = [
    "DispatcherFn",
    "Slots",
]

