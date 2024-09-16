from __future__ import annotations

import typing as t
import dataclasses as dtc

from sena import plain, seq


@dtc.dataclass(slots=True)
class Request:
    method: str
    args: dict[str, t.Any]


@dtc.dataclass(slots=True)
class Response:
    ok: t.Any


class Session(plain.Handler[Request, t.Awaitable[Response]], t.Protocol): ...


N = t.TypeVar("N", contravariant=True)


class SeqSession(seq.SeqHandler[Request, t.Awaitable[Response], N], t.Protocol): ...
