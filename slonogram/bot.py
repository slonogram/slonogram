from __future__ import annotations

from .session import Session
from .schemas import User


class Bot:
    __slots__ = ("me", "session")

    def __init__(
        self,
        me: User,
        session: Session,
    ) -> None:
        self.session = session
        self.me = me

    @classmethod
    async def from_session(cls, session: Session) -> Bot:
        raise NotImplementedError
