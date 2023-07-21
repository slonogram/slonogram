from typing import List, Optional

from .parser import parse_multiple_types, escape_hard_keywords
from .types import CodegenerationConfig, Spec, AbsolutePath
from .helpers import (
    GenerationHelper,
    Import,
    Class,
    ClassField,
    generate,
    Decorate,
    Flake8Noqa,
    IndentedLines,
)


def maybe_repr(v: Optional[str], left_none: bool) -> Optional[str]:
    if v is None:
        return "None" if not left_none else None
    return repr(v)


def generate_schemas(spec: Spec, config: CodegenerationConfig) -> str:
    schemas: List[GenerationHelper] = [
        Flake8Noqa(),
        Import("__future__", "annotations"),
        Import("enum", "Enum"),
        Import("dataclasses", "dataclass"),
        Import("typing", ("List", "Optional", "IO", "TypeAlias")),
    ]

    # Enums generation
    for name, variants in config.enums.types.items():
        fields: List[ClassField] = []
        if isinstance(variants, dict):
            for alias, rename in variants.items():
                fields.append(
                    ClassField(alias.upper(), default=repr(rename))
                )
        else:
            for alias in variants:
                fields.append(
                    ClassField(alias.upper(), default=repr(alias))
                )

        schemas.append(Class(name, [], fields, inherits=("str", "Enum")))

    unions: List[GenerationHelper] = []
    # Telegram types generation
    for ty_name, ty in spec.types.items():
        if ty_name in config.unions:
            items = config.unions[ty_name]  # type: ignore
            unions.append(
                IndentedLines(
                    [f"{ty_name}: TypeAlias = %s" % " | ".join(items)]
                )
            )
            continue
        desc = " ".join(ty.description)
        desc = f'"""{desc}"""'

        tp_fields: List[ClassField] = []
        for field in ty.fields:
            tp = parse_multiple_types(field.types, translate_io=True)
            field_name = escape_hard_keywords(field.name)
            absolute_path = AbsolutePath(f"{ty_name}.{field_name}")

            if absolute_path in config.renames:
                field_name = config.renames[absolute_path]

            if absolute_path in config.enums.overrides:
                override_tp = config.enums.overrides[absolute_path]
                tp = override_tp

            if field.required:
                tp_fields.append(
                    ClassField(
                        field_name,
                        tp,
                        maybe_repr(
                            config.defaults.get(absolute_path), True
                        ),
                    )
                )
            else:
                tp_fields.append(
                    ClassField(
                        escape_hard_keywords(field_name),
                        f"Optional[{tp}]",
                        maybe_repr(
                            config.defaults.get(absolute_path), False
                        ),
                    )
                )
        class_ = Class(ty_name, [], tp_fields)
        schemas.append(
            Decorate(
                "dataclass(slots=True)",
                class_,
            )
        )

    return generate(*schemas, *unions)
