from typing import Protocol, TypeVar, Awaitable, TYPE_CHECKING

if TYPE_CHECKING:
    from .activation import Activation
    from ..types.context import Context

M_contra = TypeVar("M_contra", contravariant=True)
R_co = TypeVar("R_co", covariant=True)

M = TypeVar("M")
R = TypeVar("R")

class GenericHandler(Protocol[M_contra, R_co]):
    def __call__(self, ctx: M_contra, /) -> Awaitable[R_co]:
        ...

class Handler(GenericHandler['Context[M]', 'Activation'], Protocol[M]):
    ...


__all__ = ["Handler", "GenericHandler"]
