import typing as t


I = t.TypeVar("I", contravariant=True)
O = t.TypeVar("O", covariant=True)
N = t.TypeVar("N", contravariant=True)

class Handler(t.Protocol[I, O]):
    def __call__(self, req: I, /) -> O:
        ...

class AsyncHandler(Handler[I, t.Awaitable[O]]):
    ...

class SeqHandler(t.Protocol[I, O, N]):
    def __call__(self, req: I, next: N, /) -> O:
        ...

class AsyncSeqHandler(SeqHandler[I, t.Awaitable[O], N]):
    ...




