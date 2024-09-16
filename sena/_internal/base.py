import typing as t

I = t.TypeVar("I", contravariant=True)
O = t.TypeVar("O", covariant=True)
N = t.TypeVar("N", contravariant=True)


class Handler(t.Protocol[I, O]):
    def __call__(self, req: I, /) -> O: ...


class Predicate(Handler[I, bool], t.Protocol[I]): ...


class SeqHandler(t.Protocol[I, O, N]):
    def __call__(self, req: I, next: N, /) -> O: ...


class SeqPredicate(SeqHandler[I, bool, N], t.Protocol[I, N]): ...
