from __future__ import annotations

from .session import Session
from .schemas import User

from ._methods import _Methods

from adaptix import Retort


def _create_retort() -> Retort:
    return Retort()


class Bot(_Methods):
    __slots__ = ("me", "session")

    def __init__(
        self,
        me: User,
        session: Session,
    ) -> None:
        self.session = session
        self.me = me

        super().__init__(_create_retort(), session)

    @classmethod
    async def from_session(cls, session: Session) -> Bot:
        rpc = _Methods(_create_retort(), session)
        return Bot(await rpc.get_me(), session)
