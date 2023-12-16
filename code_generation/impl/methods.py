from ..spec.utils import camel_to_pascal, to_snake_case
from ..spec.method import Method
from ..spec.model import SpecModel

from .extended_dataclass import ExtendedDataclass

from ..library.type_hint import Ref, TypeRefs
from ..library.type_hint.ref_sources import Source, BUILTINS

from ..library.statement import Statement
from ..library.class_ import Class
from ..library.function import Function, Argument as FunArg, self_arg
from ..library.dataclass import Dataclass, Field as DtcField
from ..library.simple import (
    FromImport,
    Definition,
    Return,
    Collection,
    AllExports,
    AddRefs,
)

from .attachs_collector import generate_collect_attachs


def generate_imports_for(stmt: Statement) -> list[Statement]:
    return [
        FromImport(source.path, list(names))
        for source, names in stmt.collect_refs().sources.items()
        if source != BUILTINS
    ]


def generate_wrapper(methods: dict[str, Method]) -> Statement:
    functions: list[Statement] = []

    for method in methods.values():
        class_name = camel_to_pascal(method.name)
        pkg_name = to_snake_case(method.name)

        required_args: list[FunArg] = []
        optional_args: list[FunArg] = []

        for arg in method.args:
            if arg.default is not None:
                optional_args.append(FunArg(arg.name, arg.type, arg.default))
            elif arg.required:
                required_args.append(FunArg(arg.name, arg.type))
            else:
                optional_args.append(FunArg(arg.name, arg.type.optional, "None"))

        create_object = f"{class_name}(%s)" % ", ".join(
            arg.name
            for arg in sorted(
                method.args, key=lambda x: not x.required or bool(x.default)
            )
        )
        call_method = (
            f"await self.session.call_method({method.name!r}, {create_object})"
        )
        functions.append(
            AddRefs(
                Function(
                    pkg_name,
                    method.return_type,
                    doc=method.doc,
                    is_async=True,
                    args=[self_arg(), *required_args, *optional_args],
                    body=[
                        Return(
                            f"self.retort.load({call_method}, {method.return_type!r})"
                        )
                    ],
                ),
                TypeRefs({Source(f"slonogram.methods.{pkg_name}"): {class_name}}),
            )
        )

    gen_cls = Class(
        "MethodWrapper",
        doc="Wrapper for calling the methods",
        body=[
            Definition("__slots__", assign="('retort', 'session')"),
            Function(
                "__init__",
                Ref(BUILTINS, "None"),
                trailing_comma=True,
                args=[
                    self_arg(),
                    FunArg("session", Ref(Source("slonogram.session"), "Session")),
                    FunArg("retort", Ref(Source("adaptix"), "Retort")),
                ],
                body=[
                    Definition("self.session", assign="session"),
                    Definition("self.retort", assign="retort"),
                ],
            ),
            *functions,
        ],
    )
    return Collection(
        [
            *generate_imports_for(gen_cls),
            gen_cls,
            AllExports([gen_cls.name]),
        ]
    )


def generate_method(method: Method, models: dict[str, SpecModel]) -> ExtendedDataclass:
    required_fields: list[DtcField] = []
    optional_fields: list[DtcField] = []

    for arg in method.args:
        if arg.default is not None:
            optional_fields.append(
                DtcField(arg.name, arg.type, doc=arg.doc, default=arg.default)
            )
        elif arg.required:
            required_fields.append(DtcField(arg.name, arg.type, doc=arg.doc))
        else:
            optional_fields.append(
                DtcField(
                    arg.name,
                    arg.type.optional,
                    doc=arg.doc,
                    default="None",
                )
            )

    return ExtendedDataclass(
        Dataclass(
            camel_to_pascal(method.name),
            [*required_fields, *optional_fields],
            doc=method.doc,
            tail=generate_collect_attachs(
                map(
                    lambda arg: (
                        arg.name,
                        arg.type.optional
                        if not arg.required or arg.default
                        else arg.type,
                    ),
                    method.args,
                ),
                models,
            ),
        )
    )
