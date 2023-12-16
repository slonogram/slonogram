from typing import Iterable

from ..spec.model import SpecModel, TypeAlias as TpAlias, PlainModel, EnumModel

from ..library.statement import Statement
from ..library.type_hint import (
    TypeRefs,
    Source,
    Union,
    TypeHint,
    reduce_refs,
    Ref,
)
from ..library.type_hint.known_refs import NONE
from ..library.type_hint.ref_sources import SCHEMAS, IO, BUILTINS
from ..library.function import Function, Argument as FunArg, self_arg
from ..library.simple import Definition, AddRefs, If, Expr


def collect_refs_recursive(
    refs: TypeRefs,
    models: dict[str, SpecModel],
    visited: set[str] | None = None,
) -> TypeRefs:
    visited = visited or set()

    for external in refs.sources.get(SCHEMAS, set()):
        if external in visited:
            break
        visited.add(external)

        model = models[external]
        if isinstance(model, TpAlias):
            refs |= collect_refs_recursive(model.alias_to.collect_refs(), models)
        elif isinstance(model, PlainModel):
            refs |= reduce_refs(
                map(
                    lambda x: collect_refs_recursive(
                        x.type.collect_refs(),
                        models,
                        visited,
                    ),
                    model.fields.values(),
                )
            )
        elif isinstance(model, EnumModel):
            refs |= TypeRefs({Source("enum"): {"StrEnum"}})

    return refs


def _is_optional(tp: TypeHint) -> bool:
    if isinstance(tp, Union):
        return NONE in tp.variants
    return False


def generate_collect_attachs(
    types: Iterable[tuple[str, TypeHint]],
    models: dict[str, SpecModel],
) -> Statement:
    defs: list[Statement] = []
    for name, tp in types:
        direct_refs = tp.collect_refs()
        if IO in direct_refs.sources:
            defs.append(
                If(
                    f"isinstance(self.{name}, IOBase)",
                    Definition(f"dest[str(id(self.{name}))]", assign=f"self.{name}"),
                )
            )
        elif IO in collect_refs_recursive(direct_refs, models).sources:
            defs.append(Expr(f"collect_attachs_from(self.{name}, dest)"))

    return AddRefs(
        Function(
            "collect_attachs",
            Ref(BUILTINS, "None"),
            args=[
                self_arg(),
                FunArg(
                    "dest",
                    Ref(BUILTINS, "dict")[Ref(BUILTINS, "str"), Ref(IO, "IOBase")],
                ),
            ],
            body=defs,
        ),
        TypeRefs({Source("slonogram._internal.utils"): {"collect_attachs_from"}}),
    )
