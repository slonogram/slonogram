from typing import (
    TypeVar,
    Callable,
    TypeAlias,
    Generic,
    Any,
)

from ..exceptions.stash import CannotProvide

T = TypeVar("T")
LazyCreate: TypeAlias = Callable[['Stash'], T]
DepsMap: TypeAlias = dict[type, 'Any | Lazy[Any]']

class _Sentinel:
    __slots__ = ()
_SENTINEL = _Sentinel()

class Lazy(Generic[T]):
    __slots__ = ('create', )

    def __init__(self, create: LazyCreate[T]) -> None:
        self.create = create


class Stash:
    __slots__ = ('parent', 'dependencies')

    def __init__(
        self,
        parent: 'Stash | None' = None,
        dependencies: DepsMap | None = None,
    ) -> None:
        self.parent = parent
        if dependencies is None:
            self.dependencies = {}
        else:
            self.dependencies = dependencies
    
    def __getitem__(self, tp: type[T]) -> T:
        value = self.dependencies.get(tp, _SENTINEL)

        if value is _SENTINEL:
            parent = self.parent
            if parent is None:
                raise CannotProvide(tp)
            return parent[tp]
        
        if isinstance(value, Lazy):
            value = value.create(self)
            self.dependencies[tp] = value
        return value  # type: ignore
    
    def __setitem__(self, key: type[T], value: T) -> None:
        self.dependencies[key] = value

    def with_parent(self, parent: 'Stash') -> 'Stash':
        return Stash(parent, self.dependencies)
    
    def merge(self, rhs: 'DepsMap | Stash') -> 'Stash':
        if isinstance(rhs, Stash):
            rhs = rhs.dependencies
        return Stash(self.parent, {**self.dependencies, **rhs})


__all__ = ["Stash", "Lazy"]
