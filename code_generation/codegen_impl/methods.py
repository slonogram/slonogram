from typing import Iterable
from functools import reduce

from .folder import fold_types

from ..spec_models.methods import Argument as MethodArg

from ..library.type_hint import (
    TypeHint,
    TypeRefs,
    Ref,
    Union,
    Parametrized,
    List,
    SCALAR_BUILTINS,
)
from ..library.function import Function, Argument, self_arg
from ..library.statement import Statement
from ..library.class_ import Class
from ..library.docs import SphinxDoc, DocRaises
from ..library.simple import (
    FromImport,
    Collection,
    Return,
    Definition,
    If,
)
from ..spec_models.methods import Method


def _is_external(tp: TypeHint) -> bool:
    if isinstance(tp, (Parametrized, List)):
        return True
    elif isinstance(tp, Ref):
        return tp.name not in SCALAR_BUILTINS and tp.name != "BinaryIO"
    elif isinstance(tp, Union):
        return any(_is_external(n) for n in tp.variants)
    raise NotImplementedError


def _repr_tp(tp: TypeHint) -> str:
    if isinstance(tp, List):
        return "list"
    if isinstance(tp, Parametrized):
        return repr(tp.type)
    return repr(tp)


def _build_external_tuple(tp: TypeHint) -> tuple[str, list[TypeHint]]:
    externals: list[TypeHint] = [tp]
    if isinstance(tp, Union):
        externals = list(filter(_is_external, tp.variants))

    if len(externals) == 1:
        return (_repr_tp(externals[0]), [tp])
    return ("(" + ", ".join(map(_repr_tp, externals)) + ")", externals)


def _add_check(
    state: If | None,
    cond: str,
    stmt: Statement,
) -> If:
    if state is None:
        return If(cond, stmt)
    return If(
        state.cond,
        state.then,
        elifs=[*state.elifs, (cond, stmt)],
    )


def _assign_adaptix(name: str, typs: list[TypeHint]) -> Definition:
    union_typ = reduce(
        lambda lhs, rhs: lhs | rhs,
        typs,
    )
    assigned_value = f"dump_json(self._retort.dump({name}, {union_typ!r}))"
    return Definition(f"args[{name!r}]", assign=assigned_value)


def _use_arg(
    arg: MethodArg,
    dict_args: list[str],
    body: list[Statement],
    tp: TypeHint,
    refs: TypeRefs,
) -> bool:
    check: If | None = None
    have_files = False
    added_ext = False

    if _is_external(tp):
        ext_check_tuple, externals = _build_external_tuple(tp)
        if len(externals) > 1:
            instance_check = f"isinstance({arg.name}, {ext_check_tuple})"
        else:
            instance_check = f"{arg.name} is not None"

        added_ext = True
        check = _add_check(
            check,
            instance_check,
            _assign_adaptix(arg.name, externals),
        )
    if "BinaryIO" in refs.typing:
        have_files = True
        check = _add_check(
            check,
            f"isinstance({arg.name}, IOBase)",
            Definition(f"files[{arg.name!r}]", assign=arg.name),
        )
    if not arg.required and not ("BinaryIO" in refs.typing or added_ext):
        check = _add_check(
            check,
            f"{arg.name} is not None",
            Definition(f"args[{arg.name!r}]", assign=arg.name),
        )

    if check is None:
        dict_args.append(f"{arg.name!r}: {arg.name}")
    else:
        body.append(check)
    return have_files


def _generate_method(method: Method) -> tuple[Statement, TypeRefs] | None:
    return_type = fold_types(method.returns)
    refs = return_type.collect_refs()

    required_args: list[Argument] = [self_arg()]
    optional_args: list[Argument] = []

    args_in_dict: list[str] = []
    param_docs: list[tuple[str, str]] = []
    body: list[Statement] = []

    files_expr = ""
    have_files = False

    for arg in method.arguments:
        hint = fold_types(arg.types)

        arg_refs = hint.collect_refs()
        refs |= arg_refs

        have_files |= _use_arg(
            arg,
            args_in_dict,
            body,
            hint,
            arg_refs,
        )

        param_docs.append((arg.name, arg.description))

        if arg.required:
            required_args.append(Argument(arg.name, hint))
        else:
            optional_args.append(Argument(arg.name, hint.optional, "None"))

    if have_files:
        body.insert(
            0, Definition("files", Ref("dict")[Ref("str"), Ref("IOBase")], "{}")
        )
    return (
        Function(
            convert_case(method.name),
            fold_types(method.returns),
            is_async=True,
            doc=repr(
                SphinxDoc(
                    "\n".join(method.description) + f"\n\nSource: {method.href}",
                    param_docs,
                    return_doc=" | ".join(method.returns),
                    raises=[
                        DocRaises(
                            "slonogram.exceptions.api.ApiError",
                            "If telegram returned an API error",
                        ),
                    ],
                    rtype=return_type,
                )
            ),
            trailing_comma=True,
            args=[*required_args, *optional_args],
            body=[
                Definition(
                    "args",
                    Ref("dict")[Ref("str"), Ref("Any")],
                    "{" + ", ".join(args_in_dict) + "}",
                ),
                *body,
                Return(
                    f"self._retort.load(await self._session.call_method({method.name!r}, args{files_expr}), {return_type!r})"
                ),
            ],
        ),
        refs,
    )


def generate_methods(methods: Iterable[Method], class_name: str) -> str:
    pythonized_methods: list[Statement] = []
    refs = TypeRefs()

    for method in methods:
        result = _generate_method(method)
        if result is None:
            continue

        stmt, m_refs = result
        refs |= m_refs
        pythonized_methods.append(stmt)

    return Collection(
        [
            FromImport("__future__", "annotations"),
            FromImport("slonogram.session", "Session"),
            FromImport("slonogram.utils", "dump_json"),
            FromImport("adaptix", "Retort"),
            FromImport("slonogram.schemas", list(refs.external)),
            FromImport("typing", list(refs.typing | {"Any"})),
            FromImport("io", "IOBase"),
            Class(
                class_name,
                body=[
                    Definition("__slots__", assign="('_session', '_retort')"),
                    Function(
                        "__init__",
                        Ref("None"),
                        args=[
                            self_arg(),
                            Argument("retort", Ref("Retort")),
                            Argument("session", Ref("Session")),
                        ],
                        body=[
                            Definition("self._retort", assign="retort"),
                            Definition("self._session", assign="session"),
                        ],
                    ),
                    *pythonized_methods,
                ],
            ),
        ]
    ).generate()


def convert_case(camel: str) -> str:
    if not camel:
        return camel
    snake = ""

    if camel[0].isupper():
        snake += camel[0].lower()
    else:
        snake += camel[0]

    for offset in range(1, len(camel)):
        char = camel[offset]
        if char.isupper():
            snake += "_" + char.lower()
            continue
        snake += char
    return snake
