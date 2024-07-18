import typing as t
import dataclasses as dtc


Scalar: t.TypeAlias = str

@dtc.dataclass(slots=True)
class Request:
    method: str
    data: dict[str, Scalar] | None = None
    files: dict[str, t.BinaryIO] | None = None


__all__ = ["Request"]

