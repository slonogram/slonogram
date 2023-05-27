from __future__ import annotations
from typing import (
    Callable,
    Awaitable,
    TypeAlias,
    TypeVar,
    Generic,
)
from inspect import iscoroutine

from ..filtering import FilterFn
from ..schemas.updates import UpdateType

T = TypeVar("T")
R = TypeVar("R")
HandlerFn: TypeAlias = Callable[[T], Awaitable[None]]


class Handler(Generic[T]):
    def __init__(
        self,
        function: HandlerFn[T],
        filter_: FilterFn[T],
        update_type: UpdateType,
    ) -> None:
        self._filter = filter_
        self._fn = function
        self._update_type = update_type

    def transform(
        self, f: Callable[[HandlerFn[T], UpdateType], Handler[R]]
    ) -> Handler[R]:
        return f(self._fn, self._update_type)

    async def handle(self, data: T) -> bool:
        data_trans = self._filter(data)
        if iscoroutine(data_trans):
            data_opt = await data_trans
        else:
            data_opt = data_trans

        # data_trans -> data_opt is needed for mypy O_o

        if data_opt is None:
            return False

        await self._fn(data_opt)

        return True

    @property
    def update_type(self) -> UpdateType:
        return self._update_type


__all__ = ["Handler", "HandlerFn", "FilterFn"]
