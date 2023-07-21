from typing import List, Dict, Tuple
from inflection import underscore, camelize

from .parser import (
    parse_type_ex,
    parse_multiple_types,
    wrap_list,
    escape_hard_keywords,
    prefix_schema,
)
from .types import (
    Spec,
    CodegenerationConfig,
    Method,
    MethodName,
    AbsolutePath,
)
from .helpers import (
    GenerationHelper,
    Function,
    FunctionArgument,
    SelfArg,
    generate,
    Import,
    Lines,
    IndentedLines,
    DocumentationString,
    DocParameter,
    Class,
    ClassField,
    Flake8Noqa,
)


def use_retort(
    expr: str, config: CodegenerationConfig, abs_path: AbsolutePath
) -> str:
    if abs_path in config.call_groups.dump:
        return f"dumps(self._session.retort.dump({expr}))"
    return expr


def mk_abs(k: str, v: str) -> AbsolutePath:
    return AbsolutePath(f"{k}.{v}")


def generate_call_group(
    cg_name: str,
    # this is for black's sake!
    cg_methods: List[MethodName],
    methods: Dict[str, Method],
    config: CodegenerationConfig,
) -> str:
    imports: List[GenerationHelper] = [
        Import("typing", ("Awaitable", "Optional", "List", "IO")),
        Import("slonogram", "schemas"),
        Import("slonogram.types.api_session", "ApiSession"),
        Import("slonogram.utils.json", "dumps"),
    ]
    body: List[Function] = [
        Function(
            "__init__",
            [
                SelfArg(),
                FunctionArgument("session", "ApiSession"),
            ],
            IndentedLines(["self._session = session"]),
            "None",
        )
    ]

    for cg_method in cg_methods:
        method = methods[cg_method]
        newlined_desc = "\n".join(method.description)
        brief = f"{newlined_desc}\nfor more: {method.href}"

        fn_args: List[FunctionArgument | SelfArg] = [SelfArg()]
        doc_params: List[DocParameter] = []
        ret_tp = parse_multiple_types(method.returns, prefix=True)

        dict_presets: List[Tuple[str, str]] = []
        fn_body: List[str] = []
        for arg in method.fields:
            absolute_path = AbsolutePath(f"{cg_method}.{arg.name}")

            match arg.types:
                case [tg_tp]:
                    r = parse_type_ex(tg_tp)
                    tp = prefix_schema(r)
                    maybe_inside = r.arg
                    union = False
                case anything:
                    tp = parse_multiple_types(anything, prefix=True)
                    maybe_inside = None
                    union = True

            if absolute_path in config.call_groups.replace_types:
                if union:
                    raise NotImplementedError(
                        f"{absolute_path} type cannot be replaced: union"
                    )
                on = (
                    "schemas."
                    + config.call_groups.replace_types[absolute_path]
                )
                tp = wrap_list(on) if maybe_inside is not None else on

            arg_name = escape_hard_keywords(arg.name)
            if arg.required:
                dict_presets.append((arg.name, arg_name))
                fn_args.append(
                    FunctionArgument(
                        arg_name,
                        tp,
                    )
                )
            else:
                fn_body.extend(
                    [
                        f"if {arg_name} is not None:"
                        f"    params[{arg.name!r}] = %s"
                        % use_retort(
                            arg_name, config, mk_abs(cg_method, arg.name)
                        ),
                        "",
                    ]
                )
                fn_args.append(
                    FunctionArgument(arg_name, f"Optional[{tp}]", "None")
                )
            doc_params.append(DocParameter(arg_name, arg.description))

        if cg_method in config.call_groups.renames:
            use_name = config.call_groups.renames[cg_method]
        else:
            use_name = cg_method
        function = Function(
            underscore(use_name),
            fn_args,
            Lines(
                [
                    DocumentationString(
                        brief,
                        doc_params,
                        "See link mentioned above for more information",
                    ),
                    IndentedLines(
                        [
                            "params: dict = {%s}"
                            % ", ".join(
                                f"{key!r}: "
                                + use_retort(
                                    value, config, mk_abs(cg_method, key)
                                )
                                for key, value in dict_presets
                            )
                        ]
                    ),
                    IndentedLines(fn_body),
                    IndentedLines(
                        [
                            f"return self._session.call_method("
                            f" {ret_tp}, {cg_method!r}, params)"
                        ]
                    ),
                ]
            ),
            return_hint=f"Awaitable[{ret_tp}]",
        )
        body.append(function)

    result = generate(
        Flake8Noqa(),
        *imports,
        Class(
            camelize(cg_name, True) + "CallGroup",
            body,
            [ClassField("__slots__", default='("_session",)')],
        ),
    )
    return result


def generate_call_groups(
    config: CodegenerationConfig, spec: Spec
) -> Dict[str, str]:
    groups: Dict[str, str] = {}

    for cg_name, cg_methods in config.call_groups.groups.items():
        groups[cg_name] = generate_call_group(
            cg_name, cg_methods, spec.methods, config
        )

    return groups
