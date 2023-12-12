from typing import Iterable
from keyword import kwlist

from .folder import fold_types

from ..library.function import Argument, Function, self_arg
from ..library.type_hint import TypeRefs, Ref
from ..library.statement import Statement
from ..library.dataclass import Dataclass, Field
from ..library.simple import (
    Collection,
    FromImport,
    TypeAlias,
    Return,
)

from ..spec_models.schemas import Model


def generate_model(model: Model) -> tuple[Statement, TypeRefs]:
    if model.subtypes and not model.fields:
        aliased_tp = fold_types(model.subtypes)
        return (
            TypeAlias(model.name, aliased_tp),
            aliased_tp.collect_refs() | TypeRefs(typing={"TypeAlias"}),
        )
    refs = TypeRefs()
    optional_fields: list[Field] = []
    required_fields: list[Field] = []

    copy_args: list[Argument] = []
    copy_bindings: list[str] = []

    for field in model.fields:
        field_name = field.name + "_" if field.name in kwlist else field.name
        hint = fold_types(field.types)
        refs |= hint.collect_refs()

        copy_args.append(
            Argument(
                field_name,
                hint | Ref("None"),
                default="None",
            )
        )
        copy_bindings.append(
            f"{field_name}=self.{field_name} if {field_name} is None else {field_name}"
        )

        if field.required:
            required_fields.append(Field(field_name, hint, field.description))
        else:
            optional_fields.append(
                Field(
                    field_name,
                    hint | Ref("None"),
                    field.description,
                    default="None",
                )
            )

    return (
        Dataclass(
            model.name,
            [*required_fields, *optional_fields],
            doc="\n".join(model.description),
            tail=(
                Function(
                    "copy_with",
                    Ref(model.name),
                    args=[self_arg(), *copy_args],
                    doc="Copies all values from the arguments (if they're not None), otherwise copies from the instance",
                    body=[
                        Return(model.name + "(" + ", ".join(copy_bindings) + ")"),
                    ],
                ),
            ),
        ),
        refs,
    )


def generate_models(models: Iterable[Model]) -> str:
    refs = TypeRefs()
    definitions: list[Statement] = []
    end: list[Statement] = []

    for model in models:
        stmt, m_refs = generate_model(model)

        refs |= m_refs
        if isinstance(stmt, TypeAlias):
            end.append(stmt)
        else:
            definitions.append(stmt)

    imports: list[Statement] = []
    if refs.typing:
        imports.append(FromImport("typing", list(refs.typing)))

    return Collection(
        [
            FromImport("__future__", "annotations"),
            *imports,
            FromImport("dataclasses", "dataclass"),
            *definitions,
            *end,
        ]
    ).generate()


__all__ = ["generate_models"]
