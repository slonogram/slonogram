from typing import (
    TypeVar,
    Iterable,
    Awaitable,
    Generic,
)

from .extended import ExtendedHandler
from .utils import unwrap_handler

from .._internal.utils import stalled
from ..types.interest import Interest
from ..types.context import Context
from ..reflect.named import get_name

from .handler import Handler
from .activation import Activation

from ..altering import Alterer1, alter1
from ..omittable import Omittable, OMIT


from ..schemas.update import Update

M = TypeVar("M")

class InterestedIn(Generic[M], ExtendedHandler[Update]):
    __slots__ = ("interests", "handler")

    def __init__(
        self,
        handler: Handler[M],
        interests: frozenset[Interest],
    ) -> None:
        self.interests = interests
        self.handler = unwrap_handler(handler)
        self.__name__ = get_name(handler, '')

    def collect_interests(self) -> frozenset[Interest]:
        return self.interests

    def alter(
        self,
        handler: Omittable[Alterer1[Handler[M]]] = OMIT,
        interests: Omittable[Alterer1[frozenset[Interest]]] = OMIT,
    ) -> 'InterestedIn[M]':
        return InterestedIn(
            handler=alter1(handler, self.handler),
            interests=alter1(interests, self.interests)
        )

    def split(self) -> Iterable['InterestedIn[M]']:
        """Splits single instance of ``InterestedIn`` into multiple instances,
        based on interests, one interest per instance.
        """

        return map(
            lambda interest: self.alter(
                interests=lambda _: frozenset((interest,)),
            ),
            self.interests,
        )
    
    def __repr__(self) -> str:
        return f"InterestedIn(interests={self.interests!r}, handler={self.handler!r})"

    def __call__(self, ctx: Context[Update]) -> Awaitable[Activation]:
        upd = ctx.model

        for interest in self.interests:
            model = getattr(upd, interest)
            if model is not None:
                return self.handler(
                    ctx.with_model(model)
                )
        return stalled()

__all__ = [
    "InterestedIn",
]
