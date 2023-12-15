from __future__ import annotations

from functools import reduce
from typing import Sequence, Iterable
from abc import ABCMeta, abstractmethod

from code_generation.library.type_hint.ref_sources import TypeRefs

from .ref_sources import TypeRefs, Source, BUILTINS


def collect_all_refs(hints: Iterable[TypeHint]) -> TypeRefs:
    return reduce(
        lambda lhs, rhs: lhs | rhs,
        map(lambda x: x.collect_refs(), hints),
        TypeRefs(),
    )


class TypeHint(metaclass=ABCMeta):
    @property
    def optional(self) -> Union:
        return self | Ref(BUILTINS, "None")

    def __or__(self, rhs: TypeHint) -> Union:
        return Union([self, rhs])

    def __repr__(self) -> str:
        return self.translate()

    def __getitem__(self, item: TypeHint | tuple[TypeHint, ...]) -> Parametrized:
        if isinstance(item, TypeHint):
            return Parametrized((item,), self)
        return Parametrized(item, self)

    @abstractmethod
    def translate(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def collect_refs(self) -> TypeRefs:
        raise NotImplementedError


class ParamSpec(TypeHint):
    def __init__(self, arg_list: list[TypeHint] | TypeHint) -> None:
        if isinstance(arg_list, TypeHint):
            self.arg_list = [arg_list]
        else:
            self.arg_list = arg_list

    def translate(self) -> str:
        return "[%s]" % ", ".join(map(repr, self.arg_list))

    def collect_refs(self) -> TypeRefs:
        return collect_all_refs(self.arg_list)


class Parametrized(TypeHint):
    def __init__(
        self,
        arguments: tuple[TypeHint, ...],
        type: TypeHint,
    ) -> None:
        self.arguments = arguments
        self.type = type

    def __getitem__(self, item: TypeHint | tuple[TypeHint, ...]) -> Parametrized:
        if isinstance(item, Parametrized):
            return Parametrized((*self.arguments, item), self.type)
        return super().__getitem__(item)

    def translate(self) -> str:
        return f"{self.type.translate()}[" + ", ".join(map(repr, self.arguments)) + "]"

    def collect_refs(self) -> TypeRefs:
        return collect_all_refs(self.arguments) | self.type.collect_refs()


class Union(TypeHint):
    def __init__(self, variants: Sequence[TypeHint]) -> None:
        if len(variants) == 0:
            raise TypeError("Union requires at least one element")

        self.variants = variants

    def translate(self) -> str:
        return " | ".join(n.translate() for n in self.variants)

    def collect_refs(self) -> TypeRefs:
        return collect_all_refs(self.variants)

    def __or__(self, rhs: TypeHint) -> Union:
        return Union([*self.variants, rhs])


class Ref(TypeHint):
    def __init__(
        self,
        source: Source,
        name: str,
    ) -> None:
        self.source = source
        self.name = name

    def translate(self) -> str:
        return self.name

    def collect_refs(self) -> TypeRefs:
        return TypeRefs({self.source: {self.name}})
