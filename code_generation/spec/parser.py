from typing import Any, TypeVar, Callable, Iterable

from ..library.type_hint.ref_sources import SCHEMAS

from . import Spec

from .folder import fold_types
from .model import (
    SpecModel,
    TypeAlias,
    PlainModel,
    Field,
)
from .utils import escape_kw
from .method import Method, Argument

T = TypeVar("T")


def _parse_field(d: dict[str, Any]) -> Field:
    return Field(
        name=escape_kw(d["name"]),
        type=fold_types(d["types"]),
        doc=d["description"],
        required=d["required"],
    )


def _collect_to_dict(f: Callable[[T], str], values: Iterable[T]) -> dict[str, T]:
    out = {}
    for value in values:
        out[f(value)] = value
    return out


def _parse_model(d: dict[str, Any]) -> SpecModel:
    name: str = d["name"]
    href: str = d["href"]
    description: list[str] = d["description"]
    raw_fields: list[Any] = d.get("fields") or []
    raw_subtypes: list[str] = d.get("subtypes") or []

    if raw_fields and raw_subtypes:
        raise NotImplementedError
    elif not raw_fields and raw_subtypes:
        return TypeAlias(
            name,
            alias_to=fold_types(raw_subtypes),
            doc="\n".join(description),
        )

    fields = {}
    for f in raw_fields:
        field = _parse_field(f)
        fields[field.name] = field

    return PlainModel(
        name=name,
        href=href,
        doc="\n".join(description),
        fields=_collect_to_dict(lambda f: f.name, map(_parse_field, raw_fields)),
    )


def _parse_argument(d: dict[str, Any]) -> Argument:
    return Argument(
        name=d["name"],
        type=fold_types(d["types"]),
        required=d["required"],
        doc=d["description"],
    )


def _parse_method(d: dict[str, Any]) -> Method:
    raw_arguments = d.get("fields") or []

    return Method(
        name=d["name"],
        href=d["href"],
        doc="\n".join(d["description"]),
        return_type=fold_types(d["returns"]),
        args=[_parse_argument(raw) for raw in raw_arguments],
    )


def parse_spec_from(d: dict[str, Any]) -> Spec:
    models = _collect_to_dict(lambda f: f.name, map(_parse_model, d["types"].values()))
    methods = _collect_to_dict(
        lambda f: f.name, map(_parse_method, d["methods"].values())
    )

    return Spec(
        version=d["version"],
        release_date=d["release_date"],
        changelog=d["changelog"],
        models=models,
        methods=methods,
    )
