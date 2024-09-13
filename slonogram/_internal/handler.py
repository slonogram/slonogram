import typing as t

import sena.plain as plain
import sena.seq as seq

from .activation import Activation
from slonogram.ctx import Ctx

D = t.TypeVar("D")
N = t.TypeVar("N")


class Handler(plain.AsyncHandler[Ctx[D], Activation]):
    ...

class SeqHandler(seq.AsyncSeqHandler[Ctx[D], Activation, N]):
    ...



