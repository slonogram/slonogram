import typing as t

import sena.plain as plain
import sena.seq as seq

from .ctx import Ctx

D = t.TypeVar("D")
N = t.TypeVar("N", contravariant=True)


class Filter(plain.Predicate[Ctx[D]], t.Protocol[D]): ...


class SeqFilter(seq.SeqPredicate[Ctx[D], N], t.Protocol[D, N]): ...
