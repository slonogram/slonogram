from .tracking import Tracker

from typing import TypeAlias, Callable
from dataclasses import dataclass

Source: TypeAlias = str

@dataclass(slots=True, frozen=True)
class Dependency:
    alias: str | None = None


def map_sources(
    source_map: dict[str, Callable[[str], str | None]],
) -> Callable[[str, str], str | None]:
    def inner(source: str, name: str) -> str | None:
        if source in source_map:
            return source_map[source](name)
        return None
    
    return inner

def _make_import_item(name: str, dep: Dependency) -> str:
    if dep.alias is not None:
        name += f" as {dep.alias}"
    
    return name

class Collector(Tracker):
    __slots__ = ('tracked', 'alias')

    def __init__(
        self,
        tracked: dict[Source, dict[str, Dependency]] | None = None,
        alias: Callable[[str, str], str | None] =
            map_sources({
                'slonogram.schemas': lambda name: f'_{name}'
            }),
    ) -> None:
        if tracked is None:
            tracked = {}

        self.tracked = tracked
        self.alias = alias

    def generate(self) -> str:
        return "\n".join(
            "from %s import %s" % (source, ', '.join(
                _make_import_item(name, dep)
                for name, dep in dependencies.items()
            ))
            for source, dependencies in self.tracked.items()
        )
    
    def generate_all(self) -> str:
        array = ""
        for deps in self.tracked.values():
            exported = ', '.join(
                repr(dep.alias or dep_name)
                for dep_name, dep in deps.items()
            )
            array += exported + ', '

        return f'[{array}]'

    def source(self, source: Source) -> dict[str, Dependency]:
        ret = self.tracked.get(source)
        if ret is None:
            ret = {}
            self.tracked[source] = ret
        
        return ret
    
    def __call__(self, source: str, name: str) -> str:
        src = self.source(source)
        dep = src.get(name)

        if dep is None:
            alias = self.alias(source, name)
            dep = Dependency(alias=alias)

            src[name] = dep

        return dep.alias or name


__all__ = [
    "Dependency",
    "Collector",
    "map_sources",
]

