from typing import Iterable

def create_stmts(stmts: Iterable[str]) -> str:
    return '\n'.join(stmts)

__all__ = ["create_stmts"]
