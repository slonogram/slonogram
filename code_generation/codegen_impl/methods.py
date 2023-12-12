from typing import Iterable
from textwrap import indent
from telegram_type_parser import fold_ex

from . import FixedStringFolder, INDENT
from ..spec_models.methods import Method, Argument

INDENT_S = " " * INDENT


def _indent(s: str) -> str:
    return indent(s, INDENT_S)


def _simply_fold(s: str) -> str:
    return fold_ex(s, FixedStringFolder(False, False))


def collect_refs(s: list[str]) -> tuple[bool, set[str]]:
    refs: set[str] = set()
    has_file: bool = False
    for tp in s:
        folder = FixedStringFolder(False, False)
        _ = fold_ex(tp, folder)
        refs.update(folder.refs)
        has_file = has_file or folder.is_file
    return (has_file, refs)


def have_file(tp: str) -> bool:
    folder = FixedStringFolder(False, False)
    _ = fold_ex(tp, folder)

    return folder.is_file


def any_file(args: list[Argument]) -> bool:
    return any(any(map(have_file, arg.types)) for arg in args)


def documentation_for(method: Method) -> str:
    params: list[str] = []

    for arg in method.arguments:
        params.append(f":param {arg.name}: {arg.description}")

    return (
        "\n".join(method.description)
        + f"\nTelegram docs: {method.href}\n\n"
        + "\n".join(params)
        + "\n:raises: `slonogram.exceptions.api.ApiError` if telegram returned an error"
        + "\n"
    )


def generate_method(method: Method) -> tuple[str, set[str]]:
    refs: set[str] = collect_refs(method.returns)[1]
    return_tp = " | ".join(map(_simply_fold, method.returns))

    converted = convert_case(method.name)

    optional_sigs: list[str] = []
    optional_binds: list[str] = []

    files_binds: list[str] = []

    required_sigs: list[str] = []
    required_args_dict: list[str] = []
    any_files: bool = any_file(method.arguments)

    def _plain_arg(v: str) -> str:
        if any_files:
            return f"str({v})"
        return v

    for argument in method.arguments:
        has_file, arg_refs = collect_refs(argument.types)
        refs.update(arg_refs)

        tps = " | ".join(map(_simply_fold, argument.types))
        base_sig = f"{argument.name}: {tps}"

        if argument.required:
            required_sigs.append(base_sig)

            if has_file:
                if len(argument.types) == 1:
                    files_binds.append(f"files[{argument.name!r}] = {argument.name}")
                else:
                    files_binds.append(
                        f"if isinstance({argument.name}, IOBase):\n"
                        f"    files[{argument.name!r}] = {argument.name}"
                    )
            else:
                required_args_dict.append(
                    f"{argument.name!r}: {_plain_arg(argument.name)}"
                )
        else:
            if has_file:
                if len(argument.types) == 1:
                    added_elif = ""
                else:
                    added_elif = (
                        f"elif {argument.name} is not None:\n"
                        f"    args[{argument.name!r}] = {_plain_arg(argument.name)}\n"
                    )
                optional_binds.append(
                    f"if isinstance({argument.name}, IOBase):\n"
                    f"    files[{argument.name!r}] = {argument.name}\n" + added_elif
                )
            else:
                optional_binds.append(
                    f"if {argument.name} is not None:\n"
                    f"    args[{argument.name!r}] = {_plain_arg(argument.name)}"
                )
            optional_sigs.append(base_sig + " | None = None")

    merged = [*required_sigs, *optional_sigs]
    required_args_dict_body = ",".join(required_args_dict)
    if required_args_dict:
        required_args_dict_body += ","

    if optional_binds:
        optionals_body = _indent("\n".join(optional_binds)) + "\n"
    else:
        optionals_body = ""
    if any_files:
        files_body = "files: dict[str, BinaryIO] = {}\n"
        files_body += "\n".join(files_binds)
        files_body = _indent(files_body) + "\n"

        files_arg = "files,"
    else:
        files_body = ""
        files_arg = ""

    # fmt: off
    df = f"await self._session.call_method({method.name!r}, args,{files_arg})"
    out = (
          f"async def {converted}(self, {','.join(merged)}) -> {return_tp}:\n"
        + _indent('"""' + documentation_for(method) + '"""\n')
        + f"    args: dict[str, Any] = {{{required_args_dict_body}}}\n"
        + files_body
        + optionals_body
        + f"    return self._retort.load({df}, {return_tp})"
    )
    # fmt: on

    return (out, refs)


def generate_methods(methods: Iterable[Method], class_name: str) -> str:
    generated_methods: list[str] = []
    to_import: set[str] = set()

    for method in methods:
        generated, refs = generate_method(method)
        to_import.update(refs)
        generated_methods.append(generated)

    # fmt: off
    if to_import:
        schemas_imports = "from slonogram.schemas import " + ",".join(to_import)
    else:
        schemas_imports = ""

    cls_s = (
        f"class {class_name}:\n"
        f"    __slots__ = ('_session', '_retort')\n\n"
        f""
        f"    def __init__(self, retort: Retort, session: Session) -> None:\n"
        f"        self._retort = retort\n"
        f"        self._session = session\n"
        f""
    )
    return (
          "from adaptix import Retort\n"
        + "from typing import BinaryIO, Any\n"
        + "from io import IOBase\n"
        + "from slonogram.session import Session\n"
        + schemas_imports + "\n"
        + "\n"
        + cls_s
        + _indent('\n'.join(generated_methods))
        + "\n\n"
        + f"__all__ = [\"{class_name}\"]"
    )
    # fmt: on


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
