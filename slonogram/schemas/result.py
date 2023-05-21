from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class Result(Generic[T]):
    ok: bool

    data: Optional[T] = None

    error_code: Optional[int] = None
    description: Optional[str] = None
