from dataclasses import dataclass, field
from typing import BinaryIO


@dataclass(slots=True)
class Request:
    method_name: str
    params: dict[str, str]
    files: dict[str, BinaryIO] = field(default_factory=dict)


__all__ = ["Request"]


