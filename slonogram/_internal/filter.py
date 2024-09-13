import typing as t

from sena import Ext
import sena.plain as plain
import sena.seq as seq

from ..ctx import Ctx

D = t.TypeVar("D")
N = t.TypeVar("N")
F = t.TypeVar("F")


class Filter(plain.Handler[Ctx[D], bool]):
    ...

# Yea, probably no one will use this (like why you would?).
class SeqFilter(seq.SeqHandler[Ctx[D], bool, N]):
    ...


