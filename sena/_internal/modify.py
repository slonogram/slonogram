import typing as t

O = t.TypeVar("O")

class Modify(t.Protocol):
    def modify(self, f: t.Callable[[t.Self], O]) -> O:
        return f(self)


__all__ = ["Modify"]

