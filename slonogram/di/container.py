from __future__ import annotations
from typing import Dict, Type, Any, Iterable, Optional, TypeVar

from ..exceptions.dependencies import DependencyIsAlreadyExistsError

T = TypeVar("T")
_SENTINEL = object()


class Container:
    _parent: Optional[Container]
    _deps: Dict[Type, Any]

    def __init__(self, parent: Optional[Container] = None) -> None:
        self._deps = {}
        self._parent = None

    def try_get_dependency(self, dep_ty: Type[T]) -> Optional[T]:
        """
        Performs single level lookup of the dependency
        """

        return self._deps.get(dep_ty)

    def try_lookup_dependency(self, dep_ty: Type[T]) -> Optional[T]:
        """
        Performs recursive lookup of the dependency
        """

        local_dep = self._deps.get(dep_ty, _SENTINEL)
        if local_dep is not _SENTINEL:
            return local_dep

        if self._parent is not None:
            return self._parent.try_lookup_dependency(dep_ty)
        return None

    def register_dependencies(self, deps: Iterable[Any]) -> None:
        for dep in deps:
            self.register_dependency(dep)

    def register_dependency(self, dep: Any) -> None:
        ty = type(dep)
        if ty in self._deps:
            raise DependencyIsAlreadyExistsError(dep)

        self._deps[ty] = dep


__all__ = ["Container"]
