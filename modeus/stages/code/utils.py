from typing import Iterable
from modeus.spec import Field


def create_method_call(
    name: str,
    fields: Iterable[Field],
    self_annot: str | None = None,
) -> str:
    return ""

__all__ = [
    "create_method_call",
]
