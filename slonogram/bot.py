import typing as t

from .utils.altering import Alterer1, alter1
from .utils.omit import Omittable, OMIT

from .session.base import SessionFn


class Bot:
    __slots__ = ('session', )

    def __init__(self, session: SessionFn) -> None:
        self.session = session

    def alter(
        self,
        *,
        session: Omittable[Alterer1[SessionFn]] = OMIT,
    ) -> t.Self:
        return type(self)(
            session=alter1(session, self.session),
        )

    def __repr__(self) -> str:
        return f"Bot(session={self.session!r})"


__all__ = ["Bot"]


