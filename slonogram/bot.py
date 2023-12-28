from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator
from io import IOBase
from adaptix import (
    Retort,
    as_is_dumper,
    dumper,
    Chain,
    name_mapping,
    P,
)

from .utils.hof import Alter1, alter1
from ._internal.adaptix import MatchFirstLayerOfFields, dump_field
from ._internal.api_wrapper import MethodsWrapper

from .session import Session, ApiGate
from .schemas import User


class Bot(MethodsWrapper):
    """Bot instance. Main telegram API interface.

    # Creation

    You can create :ref:`Bot` instance with the three ways:
    - Through passing session and the :ref:`User` instance (me)
    - Through the :ref:`Bot.from_session` classmethod, it fetches `me` automatically
    - Through the :ref:`Bot.from_aiohttp` classmethod, same as calling :ref:`Bot.from_session` with the
      :ref:`slonogram.extra.session.aiohttp` session factory, requires `slonogram[aiohttp]` extra
    """

    __slots__ = (
        "me",
        "session",
        "retort",
    )

    def __init__(
        self,
        gate_or_session: ApiGate | Session,
        me: User,
        *,
        retort: Retort | None = None,
    ) -> None:
        _retort = retort if retort is not None else _create_retort()

        if isinstance(gate_or_session, Session):
            self.session = gate_or_session
            super().__init__(gate_or_session, _retort)
        else:
            self.session = Session(
                _extend_retort(_retort),
                gate_or_session,
            )
            super().__init__(self.session, _retort)

        self.me = me

    def alter(
        self,
        session: Alter1[Session] | None = None,
        me: Alter1[User] | None = None,
        retort: Alter1[Retort] | None = None,
    ) -> Bot:
        return Bot(
            gate_or_session=alter1(session, self.session),
            me=alter1(me, self.me),
            retort=alter1(retort, self.retort),
        )

    @property
    def username(self) -> str:
        # TODO: make `self.me` type special
        return self.me.username  # type: ignore

    @classmethod
    @asynccontextmanager
    async def from_aiohttp(
        cls,
        token: str,
        *,
        endpoint: str | None = None,
    ) -> AsyncIterator[Bot]:
        """Create :ref:`Bot` from the default `aiohttp` session.

        See class-level documentation for more information.

        :param token: bot token
        :param endpoint: endpoint to use when making calls to the telegram API
        """
        from .extra.session.aiohttp import create_api_gate

        async with create_api_gate(token, endpoint=endpoint) as gate:
            yield await Bot.from_api_gate(gate)

    @classmethod
    async def from_api_gate(
        cls,
        gate: ApiGate,
    ) -> Bot:
        """Create `Bot` from the provided session factory

        See class-level documentation for more information
        """
        retort = _extend_retort(_create_retort())
        session = Session(retort, gate)

        rpc = MethodsWrapper(session, retort)
        return cls(session, await rpc.get_me())

    async def drop_pending_updates(self) -> None:
        """Drops updates from the telegram queue.

        Under the hood it's just call to the :ref:`Bot.delete_webhook`
        with `drop_pending_updates` parameter set to `True`
        """
        await self.delete_webhook(drop_pending_updates=True)


def _create_retort() -> Retort:
    return Retort(
        recipe=[
            as_is_dumper(IOBase),
            name_mapping(omit_default=~P["type"]),
        ]
    )


def _extend_retort(retort: Retort) -> Retort:
    return retort.extend(
        recipe=[
            dumper(
                MatchFirstLayerOfFields(),
                dump_field,
                Chain.LAST,
            ),
        ],
    )


__all__ = ["Bot"]
