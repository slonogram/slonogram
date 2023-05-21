from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

T = TypeVar("T")


@dataclass(slots=True)
class Result(Generic[T]):
    ok: bool

    data: Optional[T] = None

    error_code: Optional[int] = None
    description: Optional[str] = None

    def unwrap_data(self) -> T:
        if self.data is None:
            raise TypeError("unwrap failed: data is None")
        return self.data


__all__ = ["Result"]
