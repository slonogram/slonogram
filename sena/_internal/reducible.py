import typing as t

Acc = t.TypeVar("Acc")


class Reducer(t.Protocol[Acc]):
    def __call__(self, acc: Acc, item: t.Any, /) -> Acc:
        ...

@t.runtime_checkable
class Reducible(t.Protocol):
    def reduce(self, f: Reducer[Acc], initial: Acc, /) -> Acc:
        """Reduce internals to some specific value.
        Can be used to deeply inspect object dynamically.
        Left-associative.
        """


def try_reduce(x: Reducible | t.Any, f: Reducer[Acc], initial: Acc) -> Acc:
    """Reduces object if it is reducible, otherwise
    returns `initial` back.
    """
    if isinstance(x, Reducible):
        return x.reduce(f, initial)
    return initial


