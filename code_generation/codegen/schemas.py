from typing import Iterable
from textwrap import indent
from keyword import kwlist
from dataclasses import dataclass

from telegram_type_parser import fold

from . import INDENT
from ..spec_models.schemas import Model

IMPORTS: list[str] = ["dataclasses", "typing"]
IMPORTS_GENERATED: str = "\n".join(f"import {n}" for n in IMPORTS)
DTC = "@dataclasses.dataclass(slots=True)"
TQS = '"""'


@dataclass
class Class:
    output: str


@dataclass
class TypeAlias:
    output: str


def codegenerate_model(model: Model) -> Class | TypeAlias:
    if model.subtypes and not model.fields:
        return TypeAlias(
            f"{model.name}: typing.TypeAlias = " + " | ".join(map(fold, model.subtypes))
        )
    pre_cls = f"class {model.name}:\n"

    lines = "\n".join([*model.description, "", f"More info: {model.href}"])
    pre_cls += (" " * INDENT) + TQS + lines + TQS

    optional_fields = ""
    required_fields = ""

    for field in model.fields:
        name = field.name
        if name in kwlist:
            name += "_"

        tps = " | ".join(map(fold, field.types))
        pre = f"{name}: {tps}"

        if field.required:
            required_fields += pre + "\n"
            required_fields += repr(field.description) + "\n"
        else:
            optional_fields += pre + " | None = None"
            optional_fields += "\n"
            optional_fields += repr(field.description) + "\n"

    fields = required_fields + optional_fields
    if not fields:
        fields = "pass\n"

    return Class(pre_cls + "\n" + indent(fields, " " * INDENT))


def codegenerate_models(models: Iterable[Model]) -> str:
    transpiled_models = ""
    post_trans = ""

    for model in models:
        gen = codegenerate_model(model)

        if isinstance(gen, Class):
            transpiled_models += DTC + "\n"
            transpiled_models += gen.output + "\n"
        else:
            post_trans += gen.output + "\n"

    return (
        "from __future__ import annotations\n"
        + IMPORTS_GENERATED
        + "\n\n"
        + transpiled_models
        + "\n"
        + post_trans
    )


__all__ = ["codegenerate_models"]
