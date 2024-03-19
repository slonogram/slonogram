from ..utils import indent
from typing import Iterable

_EMPTY = ()
def create_if(
    condition: str,
    sub_conditions: Iterable[tuple[str, str]] | None = None,
    then: str | None = None,
    else_: str | None = None,
) -> str:
    stmt = f"if {condition}:\n"
    _then: str = then or "pass"
    stmt += indent(_then)

    for sub_cond, sub_body in sub_conditions or _EMPTY:
        sub_body = sub_body or "pass"
        stmt += f"\nelif {sub_cond}:\n" + indent(sub_body)
    
    if else_:
        stmt += "\nelse:\n" + indent(else_)

    return stmt


__all__ = ["create_if"]
