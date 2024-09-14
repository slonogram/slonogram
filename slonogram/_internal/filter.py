import typing as t

from sena import Ext
import sena.plain as plain
import sena.seq as seq

from ..ctx import Ctx

D = t.TypeVar("D")
N = t.TypeVar("N")
F = t.TypeVar("F")


class Filter(plain.Predicate[Ctx[D]]):
    ...

class SeqFilter(seq.SeqPredicate[Ctx[D], N]):
    ...


