from __future__ import annotations

import typing as t
import dataclasses as dtc

from sena import Ext
import sena.plain as plain

from ..utils.omit import Omittable, OMIT
from .api_error import ApiError

@dtc.dataclass(slots=True)
class Metrics:
    took: int

@dtc.dataclass(slots=True)
class Request:
    method: str
    args: dict[str, t.Any]


@dtc.dataclass(slots=True)
class Response:
    ok: t.Any

    metrics: Metrics | None = None


class Session(plain.AsyncHandler[Request, Response]):
    ...


class ExtSession(Ext[Session]):
    """Session-specific extensions.
    """

    def exp_retry(
        self,
        exp: float = 1.5,
        *,
        max_retries: int | None = 10,
        should_retry: Omittable[t.Callable[[ApiError], bool]] = OMIT,
    ) -> ExtSession:
        """Does exponential retries.
        """
        raise NotImplementedError

