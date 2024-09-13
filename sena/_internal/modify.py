import typing as t

Fst = t.TypeVar("Fst")
Ts = t.TypeVarTuple("Ts")
R = t.TypeVar("R")

O = t.TypeVar("O")

class Modify(t.Protocol):
    """Simple extension that allows calling plain functions
    in a suffix way.
    """

    @classmethod
    def partial(
        cls: t.Callable[[Fst, *Ts], R],
        *args: t.Unpack[Ts],
    ) -> t.Callable[[Fst], R]:
        return lambda fst: cls(fst, *args)

    def modify(self, f: t.Callable[[t.Self], O]) -> O:
        """Simply calls provided function on self, returns
        its value back.
        """
        return f(self)


__all__ = ["Modify"]

