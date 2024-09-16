import typing as t

from sena import plain, seq
from sena.control import ControlFlow

from .activation import Activation
from .ctx import Ctx

D = t.TypeVar("D")
N = t.TypeVar("N", contravariant=True)

Result: t.TypeAlias = ControlFlow[Ctx[D], Activation]


class Handler(plain.Handler[Ctx[D], t.Awaitable[Result[D]]], t.Protocol[D]): ...


class SeqHandler(
    seq.SeqHandler[Ctx[D], t.Awaitable[Result[D]], N], t.Protocol[D, N]
): ...
