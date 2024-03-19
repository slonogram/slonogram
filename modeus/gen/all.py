from typing import Iterable
from .variable import create_variable

def create_all(items: Iterable[str]) -> str:
    return create_variable(
        '__all__',
        value='[%s]' % ', '.join(map(repr, items)),
    )

__all__ = ["create_all"]

