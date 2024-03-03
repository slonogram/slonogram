from typing import Protocol, TypeVar, Awaitable
from abc import abstractmethod

from ..filtering import Filter
from ..dispatching.context import Context
from ..handling.activation import Activation
from ..handling.handler import Handler


M = TypeVar("M")

class Middlewared(Handler[M]):
    def __lshift__(self, rhs: 'NextMiddleware[M]') -> 'Middlewared[M]':
        from .follows import Follows

        return Follows(self, rhs)

    def __and__(self, filter: Filter[M]) -> 'Middlewared[M]':
        return self.filtered(filter)

    def __matmul__(self, filter: Filter[M]) -> 'Middlewared[M]':
        return self.filtered(filter)
    
    def const(self, value: Activation) -> 'Middlewared[M]':
        from .const import Const

        if isinstance(self, Const):
            return Const(self.handler, value)

        return Const(self, value)

    def never_activate(self) -> 'Middlewared[M]':
        return self.const(Activation.stalled())

    def always_activate(self) -> 'Middlewared[M]':
        return self.const(Activation(self))

    def filtered(self, filter: Filter[M]) -> 'Middlewared[M]':
        from .filtered import Filtered

        return Filtered(self, filter)

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplemented

class NextMiddleware(Protocol[M]):
    def __call__(self, ctx: Context[M], next: Handler[M], /) -> Awaitable[Activation]:
        ...


__all__ = ["Middlewared", "NextMiddleware"]

