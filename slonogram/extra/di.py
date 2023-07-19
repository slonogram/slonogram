from functools import partial
from inspect import Parameter
from typing import (
    Any,
    Dict,
    Mapping,
    TypeVar,
    Generic,
    Tuple,
    Callable,
    TypeAlias,
    List,
    get_origin,
)

from slonodi.container import Container
from slonodi.specifiers import DeferredEvaluation
from slonodi.injector import Provider, Injector

from ..bot import Bot

from ..types.model_types import MODEL_TYPES
from ..types.scratch import Scratch
from ..types.context import Context

T = TypeVar("T")
R = TypeVar("R")
_EMPTY_DICT: dict = {}


def create_injector() -> Injector:
    return Injector(
        SlonodiProvider(),
        default_specifiers=(DefaultSpecifier(),),
    )


NameItem: TypeAlias = Tuple[str, Callable[[Context[T]], Any]]


def _bot(context: Context[Any]) -> Bot:
    return context.inter.bot


def _identity(v: T) -> T:
    return v


def _model(context: Context[T]) -> T:
    return context.model


class DefaultSpecifier:
    def _deferred(
        self,
        names: Tuple[NameItem[Any], ...],
        context: Context[Any],
    ) -> Dict[str, Any]:
        return {name: getter(context) for name, getter in names}

    def write_dependencies(
        self, params: Mapping[str, Parameter], _: Container
    ) -> Dict[str, Any] | Tuple[Dict[str, Any], DeferredEvaluation]:
        names: List[NameItem[Any]] = []
        for name, param in params.items():
            annot = param.annotation
            origin = get_origin(annot)

            if annot is Bot:
                names.append((name, _bot))
            elif origin is Context:
                names.append((name, _identity))
            elif annot in MODEL_TYPES:
                names.append((name, _model))

        return (_EMPTY_DICT, partial(self._deferred, tuple(names)))


class SlonodiProvider(Provider[Context[Any]]):
    def provide_ctx(self, data: Any) -> Context[Any]:
        print(data)
        return data

    def provide_container(self, ctx: Context[Any]) -> Container:
        return ctx.inter.data


class FromScratchSpecifier(Generic[T, R]):
    __slots__ = ("scratch", "name")

    def __init__(self, name: str, scratch: Scratch[T, R]) -> None:
        self.scratch = scratch
        self.name = name

    def _deferred(self, context: Context[T]) -> Dict[str, Any]:
        return {self.name: context.pad[self.scratch]}

    def write_dependencies(
        self, _: Mapping[str, Parameter], __: Container
    ) -> Dict[str, Any] | Tuple[Dict[str, Any], DeferredEvaluation]:
        return (_EMPTY_DICT, self._deferred)


def from_scratch(
    name: str, scratch: Scratch[T, R]
) -> FromScratchSpecifier[T, R]:
    return FromScratchSpecifier(name, scratch)
