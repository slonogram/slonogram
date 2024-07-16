import typing as t

from .base import EndpointFn, SeqEndpointFn, EndpointFnFactory

B_co = t.TypeVar("B_co", covariant=True)
C_contra = t.TypeVar("C_contra", contravariant=True)


class After(EndpointFn[B_co, C_contra]):
    __slots__ = ('current', 'next')

    def __init__(self, current: SeqEndpointFn[B_co, C_contra], next: EndpointFn[B_co, C_contra]) -> None:
        self.current = current
        self.next = next

    @classmethod
    def factory(cls, current: SeqEndpointFn[B_co, C_contra]) -> EndpointFnFactory[B_co, C_contra, B_co, C_contra]:
        return lambda next: cls(current, next)

    def __call__(self, req: C_contra, /) -> t.Awaitable[B_co]:
        return self.current(req, self.next)

    def __repr__(self) -> str:
        return f"After(current={self.current!r}, next={self.next!r})"


__all__ = ["After"]


