from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Callable, AsyncIterator
from io import IOBase
from adaptix import (
    Retort,
    as_is_dumper,
    dumper,
    Chain,
    name_mapping,
    P,
)

from ._internal.adaptix_dumper import MatchFirstLayerOfFields, dump_field
from ._internal.api_wrapper import MethodsWrapper

from .session import Session
from .schemas import User


class Bot(MethodsWrapper):
    """Bot instance. Main telegram API interface.

    # Creation

    You can create Bot instance with the three ways:
    - Through passing session and the `User` instance (me)
    - Through the `Bot.from_session` classmethod, it fetches `me` automatically
    - Through the `Bot.from_aiohttp` classmethod, same as calling `Bot.from_session` with the
      `slonogram.extra.session.aiohttp` session factory, requires `slonogram[aiohttp]` extra
    """

    __slots__ = ("me", "session")

    def __init__(
        self,
        session_or_factory: Callable[[Retort], Session] | Session,
        me: User,
        *,
        retort: Retort | None = None,
    ) -> None:
        _retort = retort if retort is not None else _create_retort()
        if isinstance(session_or_factory, Session):
            self.session = session_or_factory
            super().__init__(session_or_factory, _retort)
        else:
            self.session = session_or_factory(_extend_retort(_retort))
            super().__init__(self.session, _retort)

        self.me = me

    @property
    def username(self) -> str:
        # TODO: make `self.me` type special
        return self.me.username  # type: ignore

    @classmethod
    @asynccontextmanager
    async def from_aiohttp(
        cls,
        token: str,
        base_url: str | None = None,
    ) -> AsyncIterator[Bot]:
        """Create `Bot` from the default `aiohttp` session.

        See class-level documentation for more information
        """
        from .extra.session.aiohttp import create_session_factory

        async with create_session_factory(token, base_url) as factory:
            yield await Bot.from_session(factory)

    @classmethod
    async def from_session(
        cls,
        session_factory: Callable[[Retort], Session],
    ) -> Bot:
        """Create `Bot` from the provided session factory

        See class-level documentation for more information
        """
        retort = _extend_retort(_create_retort())
        session = session_factory(retort)

        rpc = MethodsWrapper(session, retort)
        return cls(session, await rpc.get_me())


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
