from __future__ import annotations

from typing import Callable
from io import IOBase
from adaptix import (
    Retort,
    as_is_dumper,
    dumper,
    Chain,
    name_mapping,
)

from ._internal.adaptix_dumper import MatchFirstLayerOfFields, dump_field
from ._internal.api_wrapper import MethodWrapper

from .session import Session
from .schemas import User


class Bot(MethodWrapper):
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

    @classmethod
    async def from_session(cls, session_factory: Callable[[Retort], Session]) -> Bot:
        retort = _extend_retort(_create_retort())
        session = session_factory(retort)

        rpc = MethodWrapper(session, retort)
        return cls(session, await rpc.get_me())


def _create_retort() -> Retort:
    return Retort(
        recipe=[
            name_mapping(omit_default=True),
        ]
    )


def _extend_retort(retort: Retort) -> Retort:
    return retort.extend(
        recipe=[
            as_is_dumper(IOBase),
            dumper(
                MatchFirstLayerOfFields(),
                dump_field,
                Chain.LAST,
            ),
        ],
    )


__all__ = ["Bot"]
