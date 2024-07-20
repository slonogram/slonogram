from __future__ import annotations

import typing as t

from sena.handling.extended import (
    Handler as SenaHandler,
)
from sena.handling.base import (
    HandlerFnFactory as SenaHandlerFnFactory,
    HandlerFn as SenaHandlerFn,
    Next as SenaNext,
)
from sena.handling.simple import Simple as SenaSimple

from slonogram.filtering.filter import FilterFn
from slonogram.filtering.and_ import And

from slonogram.utils.omit import Omittable, OMIT, non_omitted_or

from slonogram.types.ctx import Ctx
from slonogram.types.activation import Activation

from slonogram.schemas.message import Message


D = t.TypeVar("D")

class _HasName(t.Protocol):
    __name__: str

class _CombineFilters(t.Protocol[D]):
    def __call__(self, lhs: FilterFn[D], rhs: FilterFn[D], /) -> FilterFn[D]:
        ...

class AbstractHandler(SenaHandler[Activation, Ctx[D]], t.Protocol[D]):
    @t.overload
    def command(
        self: _HasNameAndIs[Message],
        *,
        filter: Omittable[FilterFn[D]] = OMIT,
        combine_using: Omittable[_CombineFilters[D]] = OMIT,
    ) -> AbstractHandler[D]:
        ...

    @t.overload
    def command(
        self: AbstractHandler[Message],
        variations: t.Iterable[str] | str,
        *,
        filter: Omittable[FilterFn[D]] = OMIT,
        combine_using: Omittable[_CombineFilters[D]] = OMIT,
    ) -> AbstractHandler[D]:
        ...

    def command(
        self: AbstractHandler[Message],
        variations: Omittable[t.Iterable[str] | str] = OMIT,
        *,
        filter: Omittable[FilterFn[D]] = OMIT,
        combine_using: Omittable[_CombineFilters[D]] = OMIT,
    ) -> AbstractHandler[D]:
        _name: tuple[str, ...]

        if hasattr(self, '__name__'):
            _name = (self.__name__, )
        elif variations is not OMIT:
            if isinstance(variations, str):
                _name = (variations, )
            else:
                _name = tuple(t.cast(t.Iterable[str], variations))
        else:
            raise TypeError("Cannot use {self} as command, handler either must have a `__name__` or variations must be specified")
        _combine_using = non_omitted_or(combine_using, And)

        raise NotImplementedError

class _HasNameAndIs(_HasName, AbstractHandler[D], t.Protocol[D]):
    ...

class Handler(SenaSimple[Activation, Ctx[D]], AbstractHandler[D]):
    ...

class HandlerFn(SenaHandlerFn[Activation, Ctx[D]], t.Protocol[D]):
    ...

class HandlerFnFactory(SenaHandlerFnFactory[Activation, Ctx[D], Activation, Ctx[D]], t.Protocol[D]):
    ...

class Next(SenaNext[Activation, Ctx[D]], t.Protocol[D]):
    ...


__all__ = [
    "AbstractHandler",
    "Handler",
    "Next",
    "HandlerFn",
    "HandlerFnFactory",
]


