from typing import Iterable

def parametrize(what: str, args: str | Iterable[str]) -> str:
    if isinstance(args, str):
        args = (args, )

    return "%s[%s]" % (what, ', '.join(args))

__all__ = [
    "parametrize",
]
