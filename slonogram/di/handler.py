from typing import (
    Callable,
    Awaitable,
    Type,
    Optional,
    List,
    Any,
    Dict,
    TypeVar,
)

from array import array
from inspect import signature, Parameter

from ..exceptions.dependencies import UnsupportedArgKindError
from .container import Container

T = TypeVar("T")


class _LazyInject:
    __slots__ = ("ty",)

    def __init__(self, ty: Type) -> None:
        self.ty = ty


class _CompiledCallable:
    __slots__ = (
        "positional",
        "keyword",
        "lazy_positional_indices",
        "lazy_keyword",
    )

    def __init__(
        self,
        positional: List[Any],
        keyword: Dict[str, Any],
        lazy_pos_indices: array[int],
        lazy_kws: Dict[str, Type],
    ) -> None:
        self.positional = positional
        self.keyword = keyword

        self.lazy_positional_indices = lazy_pos_indices
        self.lazy_keyword = lazy_kws


class InjectableHandler:
    _compiled: Optional[_CompiledCallable]

    def __init__(self, callable_: Callable[..., Awaitable[None]]) -> None:
        self._callable = callable_
        self._compiled = None

    def execute(self, context: Container) -> Awaitable[None]:
        raise NotImplementedError

    def compile(
        self, container: Container, extra: Optional[Container] = None
    ) -> None:
        def lookup_for(dep_ty: Type[T]) -> T | _LazyInject:
            container_dep = container.try_lookup_dependency(dep_ty)
            if container_dep is None:
                if extra is None:
                    return _LazyInject(dep_ty)
                return extra.try_lookup_dependency(dep_ty) or _LazyInject(
                    dep_ty
                )
            else:
                return container_dep

        sig = signature(self._callable)

        lazy_kws = {}
        lazy_pos_indices = array("L")

        kw_args = {}
        pos_args = []

        index = 0
        for par_name, parameter in sig.parameters.items():
            if parameter.kind in (
                Parameter.VAR_KEYWORD,
                Parameter.VAR_POSITIONAL,
            ):
                raise UnsupportedArgKindError(
                    self._callable.__name__, parameter
                )

            dependency = lookup_for(parameter.annotation)
            if parameter.kind == Parameter.KEYWORD_ONLY:
                if isinstance(dependency, _LazyInject):
                    lazy_kws[par_name] = dependency.ty
                else:
                    kw_args[par_name] = dependency
            else:
                if isinstance(dependency, _LazyInject):
                    lazy_pos_indices.append(index)

                pos_args.append(dependency)

            index += 1

        self._compiled = _CompiledCallable(
            pos_args, kw_args, lazy_pos_indices, lazy_kws
        )


__all__ = ["InjectableHandler"]
