from __future__ import annotations
import typing

from dataclasses import dataclass

from ..library.type_hint import TypeHint


@dataclass
class Field:
    name: str
    doc: str
    type: TypeHint

    required: bool
    default: str | None = None


@dataclass
class PlainModel:
    name: str
    href: str
    doc: str
    fields: dict[str, Field]


@dataclass
class EnumModel:
    name: str
    variants: list[str | tuple[str, str]]

    def variant(self, value: str) -> EnumModel:
        return EnumModel(self.name, [*self.variants, value])


@dataclass
class TypeAlias:
    name: str
    doc: str
    alias_to: TypeHint

    def __or__(self, rhs: TypeAlias | TypeHint) -> TypeAlias:
        if isinstance(rhs, TypeAlias):
            return TypeAlias(
                self.name,
                self.doc,
                alias_to=self.alias_to | rhs.alias_to,
            )
        return TypeAlias(
            self.name,
            self.doc,
            alias_to=self.alias_to | rhs,
        )


SpecModel: typing.TypeAlias = PlainModel | TypeAlias | EnumModel
