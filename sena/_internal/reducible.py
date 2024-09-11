import typing as t

Acc = t.TypeVar("Acc")


class Reducer(t.Protocol[Acc]):
    def __call__(self, acc: Acc, item: t.Any, /) -> Acc:
        ...


class Reducible(t.Protocol):
    def reduce(self, f: Reducer[Acc], initial: Acc, /) -> Acc:
        """Reduce internals to some specific value.
        Can be used to deeply inspect object dynamically.
        Left-associative.
        """


