from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from ..session import AllowedType


@dataclass(slots=True)
class ErrorDetails:
    code: int
    description: str


class ApiError(Exception):
    __slots__ = ("method_name", "method_args", "error")

    def __init__(
        self,
        method_name: str,
        args: dict[str, AllowedType],
        error: ErrorDetails,
    ) -> None:
        super().__init__(
            f"Failed to call {method_name}: {error.description} (code {error.code})"
        )

        self.method_name = method_name
        self.method_args = args

        self.details = error
