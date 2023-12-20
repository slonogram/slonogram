from __future__ import annotations

from typing import Generic, TypeVar
from dataclasses import dataclass

T = TypeVar("T")


@dataclass(slots=True)
class ErrorDetails:
    code: int
    description: str


class ApiError(Generic[T], Exception):
    __slots__ = ("method_name", "method_args", "details")

    def __init__(
        self,
        method_name: str,
        args: T,
        error: ErrorDetails,
    ) -> None:
        super().__init__(
            f"Failed to call {method_name}: {error.description} (code {error.code})"
        )

        self.method_name = method_name
        self.method_args = args

        self.details = error
