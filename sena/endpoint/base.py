import typing as t


C_contra = t.TypeVar("C_contra", contravariant=True)
B_co = t.TypeVar("B_co", covariant=True)

C = t.TypeVar("C")
B = t.TypeVar("B")

B_contra = t.TypeVar("B_contra", contravariant=True)
C_co = t.TypeVar("C_co", covariant=True)

Bn = t.TypeVar("Bn", covariant=True)
Cn = t.TypeVar("Cn", contravariant=True)

class EndpointFn(t.Protocol[B_co, C_contra]):
    def __call__(self, req: C_contra, /) -> t.Awaitable[B_co]:
        ...

class EndpointFnFactory(t.Protocol[B_contra, C_co, Bn, Cn]):
    def __call__(self, previous: EndpointFn[B_contra, C_co]) -> EndpointFn[Bn, Cn]:
        ...

class SeqEndpointFn(t.Protocol[B, C]):
    def __call__(self, req: C, next: EndpointFn[B, C], /) -> t.Awaitable[B]:
        ...


__all__ = [
    "EndpointFn",
    "EndpointFnFactory",
    "SeqEndpointFn",
]


