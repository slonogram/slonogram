import typing as t

from sena import plain, seq

from .handler import Handler, SeqHandler

D = t.TypeVar("D")
N = t.TypeVar("N", contravariant=True)


class HandlerExt(plain.HandlerExt, t.Protocol): ...


class ExtendedHandler(HandlerExt, Handler[D], t.Protocol[D]): ...


class SeqHandlerExt(seq.SeqHandlerExt, t.Protocol): ...


class ExtendedSeqHandler(SeqHandlerExt, SeqHandler[D, N], t.Protocol[D, N]): ...
