from __future__ import annotations
from copy import copy

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Source:
    path: str


@dataclass
class TypeRefs:
    sources: dict[Source, set[str]] = field(default_factory=dict)

    @classmethod
    def typing(cls, values: set[str]) -> TypeRefs:
        return cls({TYPING: values})

    @classmethod
    def schemas(cls, values: set[str]) -> TypeRefs:
        return cls({SCHEMAS: values})

    @classmethod
    def builtins(cls, values: set[str]) -> TypeRefs:
        return cls({BUILTINS: values})

    @classmethod
    def io(cls, values: set[str]) -> TypeRefs:
        return cls({IO: values})

    def __or__(self, rhs: TypeRefs) -> TypeRefs:
        shallow = copy(self.sources)

        for source, types in rhs.sources.items():
            known_source = shallow.get(source)
            if known_source is None:
                shallow[source] = types
            else:
                shallow[source] = {*known_source, *types}

        return TypeRefs(shallow)


BUILTINS = Source("builtins")
SCHEMAS = Source("slonogram.schemas")
TYPING = Source("typing")
IO = Source("io")
