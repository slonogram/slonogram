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

INDENT_S = " " * INDENT


@dataclass
class Class:
    output: str


@dataclass
class TypeAlias:
    output: str


@dataclass
class _CopyWithArg:
    arg: str
    tp: str


@dataclass
class _CopyWith:
    args: list[_CopyWithArg]

    def generate(self, cls_name: str) -> str:
        args: list[str] = []
        checked_fields: list[str] = []

        for arg in self.args:
            args.append(f"{arg.arg}: {arg.tp} | None = None")
            checked_fields.append(
                f"{arg.arg}=self.{arg.arg} if {arg.arg} is None else {arg.arg}"
            )

        args_j = ",".join(args)
        checked_fields_j = ",".join(checked_fields)
        return f"def copy_with(self,{args_j}) -> {cls_name}:\n" + indent(
            f"return {cls_name}({checked_fields_j})", INDENT_S
        )


def codegenerate_model(model: Model) -> Class | TypeAlias:
    if model.subtypes and not model.fields:
        return TypeAlias(
            f"{model.name}: typing.TypeAlias = " + " | ".join(map(fold, model.subtypes))
        )
    pre_cls = f"class {model.name}:\n"

    lines = "\n".join([*model.description, "", f"More info: {model.href}"])
    pre_cls += INDENT_S + TQS + lines + TQS

    optional_fields = ""
    required_fields = ""
    copy_with = _CopyWith([])

    for field in model.fields:
        name = field.name
        if name in kwlist:
            name += "_"

        tps = " | ".join(map(fold, field.types))
        pre = f"{name}: {tps}"

        copy_with.args.append(_CopyWithArg(name, tps))

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

    copy_with_impl = ""
    if copy_with.args:
        copy_with_impl += "\n" + indent(copy_with.generate(model.name), INDENT_S)

    return Class(pre_cls + "\n" + indent(fields, " " * INDENT) + copy_with_impl)


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
