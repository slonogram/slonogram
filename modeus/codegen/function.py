from typing import Iterable

from ..utils import indent

def create_function(
    name: str,
    args: Iterable[str],
    body: str,
    ret_annot: str | None = None,
) -> str:
    if not body:
        body = "pass"

    args_joined = ', '.join(args)
    ret_annot_val = '' if ret_annot is None else f' -> {ret_annot}'
    return (
        f"def {name}({args_joined}){ret_annot_val}:\n"
        + indent(body)
    )

__all__ = ["create_function"]
