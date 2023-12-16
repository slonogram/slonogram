from code_generation.library.statement import Statement
from code_generation.library.function import Function, Argument as FunArg, self_arg
from code_generation.library.type_hint import TypeRefs, Ref, Source
from code_generation.library.type_hint.ref_sources import TYPING
from code_generation.library.class_ import Class
from code_generation.library.simple import Collection, Definition, AddRefs, Return

from code_generation.spec.utils import to_snake_case
from code_generation.spec.method import Method

from .cfg import METHOD_CALLS

TYPES = Source("types")
ELLIPSIS = Ref(TYPES, "EllipsisType")


def generate_shortcuts_def(methods: dict[str, Method]) -> Statement:
    functions: list[Statement] = []

    for call_name, method_ref in METHOD_CALLS.items():
        required_args: list[FunArg] = []
        optional_args: list[FunArg] = []

        source_method = methods[method_ref.alias_to]
        source_function = to_snake_case(source_method.name)
        forward_call_args: list[str] = []

        for arg in source_method.args:
            if not arg.required:
                required = False
                farg = FunArg(arg.name, arg.type.optional, "None")
            else:
                required = True
                farg = FunArg(arg.name, arg.type)

            if arg.name in method_ref.replace_field_value:
                replace_with = method_ref.replace_field_value[arg.name]
                farg.type |= ELLIPSIS  # type: ignore
                farg.default = "..."

                forward_call_args.append(
                    f"{arg.name}={replace_with} if {arg.name} is ... else {arg.name}"
                )
                required = False
            else:
                forward_call_args.append(f"{arg.name}={arg.name}")

            if required:
                required_args.append(farg)
            else:
                optional_args.append(farg)

        functions.append(
            Function(
                call_name,
                Ref(TYPING, "Awaitable")[source_method.return_type],
                doc=f"Alias to the `Bot.{source_function}` with usable defaults, for more, see `Bot.{source_function}` docs",
                args=[self_arg(method_ref.self_type), *required_args, *optional_args],
                body=[
                    Return(
                        f"self.rpc.{source_function}(%s)" % ", ".join(forward_call_args)
                    ),
                ],
            )
        )

    return AddRefs(
        Collection(
            [
                Definition("M", assign="TypeVar('M')"),
                Class(
                    "GeneratedShortcuts",
                    inherits=["AbstractContext[M]"],
                    body=functions,
                ),
            ]
        ),
        TypeRefs(
            {
                TYPING: {"TypeVar"},
                Source("slonogram.abstract.context"): {"AbstractContext"},
            }
        ),
    )
