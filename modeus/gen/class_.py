from typing import Iterable
from ..utils import indent

def create_derive(derives: Iterable[str]) -> str:
    return "(" + ",".join(derives) + ")"

def create_class(
    name: str,
    body: str | None = None,
    derive: Iterable[str] | None = None,
) -> str:
    derives = "" if derive is None else create_derive(derive)
    stmt = f"class {name}{derives}:\n"
    _body = body or "pass"
    stmt += indent(_body)

    return stmt

__all__ = ["create_class", "create_derive"]
