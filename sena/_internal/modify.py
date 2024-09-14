import typing as t

Fst = t.TypeVar("Fst")
Ts = t.TypeVarTuple("Ts")
R = t.TypeVar("R")

O = t.TypeVar("O")

@t.runtime_checkable
class Modify(t.Protocol):
    """Simple extension that allows calling plain functions
    in a suffix way.
    """

    def modify(self, f: t.Callable[[t.Self], O]) -> O:
        """Simply calls provided function on self, returns
        its value back.
        """
        return f(self)


__all__ = ["Modify"]

