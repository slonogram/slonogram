from enum import IntEnum, auto

from ..spec import Spec
from ..spec.model import (
    PlainModel,
    SpecModel,
    EnumModel,
    TypeAlias,
)

from ..library.function import (
    Function,
    Argument as FunArg,
    self_arg,
)
from ..library.dataclass import Dataclass, Field as DtcField
from ..library.enum import Enum
from ..library.type_hint import Ref
from ..library.type_hint.ref_sources import (
    TypeRefs,
    Source,
    SCHEMAS,
    BUILTINS,
)
from ..library.statement import Statement
from ..library.simple import (
    Return,
    Collection,
    FromImport,
    UseFeature,
    TypeAlias as CodegenTypeAlias,
)

from .attachs_collector import generate_collect_attachs


class Order(IntEnum):
    TOP_LEVEL = auto()
    FIRST = auto()
    LAST = auto()


ELLIPSIS_TYPE = Ref(Source("types"), "EllipsisType")
ALTER_FN = Ref(Source("slonogram.utils.hof"), "Alter1")


def _helper_methods_for(model: PlainModel, models: dict[str, SpecModel]) -> Statement:
    copy_with_args: list[FunArg] = []
    copy_with_binds: list[str] = []

    alter_args: list[FunArg] = []
    alter_binds: list[str] = []

    for name, field in model.fields.items():
        typ = field.type if field.required else field.type.optional
        copy_with_args.append(FunArg(name, typ | ELLIPSIS_TYPE, default="..."))
        copy_with_binds.append(f"{name}={name} if {name} is not ... else self.{name}")

        alterer_tp = ALTER_FN[typ]
        alter_args.append(FunArg(name, alterer_tp | ELLIPSIS_TYPE, default="..."))

        alter_binds.append(
            f"{name}=self.{name} if {name} is ... else prefer({name}(self.{name}), self.{name})"
        )

    return Collection(
        [
            generate_collect_attachs(
                map(lambda f: (f.name, f.type), model.fields.values()),
                models,
            ),
            Function(
                "alter",
                Ref(SCHEMAS, model.name),
                doc="Alters every type with the provided callable, if callable returns ... - field left untouched",
                args=[self_arg(), *alter_args],
                trailing_comma=True,
                body=[Return(f"{model.name}(%s)" % ", ".join(alter_binds))],
            ),
            Function(
                "copy_with",
                Ref(SCHEMAS, model.name),
                doc="Replaces some of model's fields with provided ones",
                args=[self_arg(), *copy_with_args],
                trailing_comma=True,
                body=[
                    Return(f"{model.name}(%s)" % ", ".join(copy_with_binds)),
                ],
            ),
        ]
    )


def _enum(model: EnumModel) -> Statement:
    return Enum(
        model.name,
        model.variants,  # type: ignore
    )


def _plain(model: PlainModel, models: dict[str, SpecModel]) -> Statement:
    required_fields: list[DtcField] = []
    optional_fields: list[DtcField] = []

    for name, field in model.fields.items():
        if field.default is not None:
            optional_fields.append(
                DtcField(
                    name,
                    field.type,
                    doc=field.doc,
                    default=field.default,
                )
            )
        elif field.required:
            required_fields.append(
                DtcField(
                    name,
                    field.type,
                    doc=field.doc,
                )
            )
        else:
            optional_fields.append(
                DtcField(
                    name,
                    field.type.optional,
                    doc=field.doc,
                    default="None",
                )
            )

    return Dataclass(
        name=model.name,
        fields=[*required_fields, *optional_fields],
        doc=model.doc,
        tail=_helper_methods_for(model, models),
    )


def _type_alias(model: TypeAlias) -> Statement:
    return CodegenTypeAlias(
        model.name,
        model.alias_to,
        doc=model.doc,
    )


def _generate_model(
    model: SpecModel, models: dict[str, SpecModel]
) -> tuple[Order, Statement]:
    if isinstance(model, EnumModel):
        return (Order.FIRST, _enum(model))
    elif isinstance(model, PlainModel):
        return (Order.FIRST, _plain(model, models))
    elif isinstance(model, TypeAlias):
        return (Order.LAST, _type_alias(model))
    raise NotImplementedError


def generate_schemas(spec: Spec) -> Statement:
    top_level: list[Statement] = []
    first_stmts: list[Statement] = []
    last_stmts: list[Statement] = []
    refs = TypeRefs()

    _dispatch_dict = {
        Order.FIRST: first_stmts,
        Order.LAST: last_stmts,
        Order.TOP_LEVEL: top_level,
    }

    for model in spec.models.values():
        order, stmt = _generate_model(model, spec.models)
        _dispatch_dict[order].append(stmt)
        refs |= stmt.collect_refs()

    imports_from_sources = [
        FromImport(source.path, tuple(names))
        for source, names in refs.sources.items()
        if source not in (BUILTINS, SCHEMAS)
    ]

    return Collection(
        (
            UseFeature("annotations"),
            FromImport("slonogram._internal.utils", "prefer"),
            *imports_from_sources,
            *top_level,
            *first_stmts,
            *last_stmts,
        )
    )
