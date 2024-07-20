import typing as t
import dataclasses as dtc

from ..utils.altering import Alterer1, alter1
from ..utils.omit import OMIT, Omittable

from .request import Request


@dtc.dataclass(slots=True)
class ErrorDetails:
    code: int
    description: str

    def alter(
        self,
        *,
        code: Omittable[Alterer1[int]] = OMIT,
        description: Omittable[Alterer1[str]] = OMIT,
    ) -> t.Self:
        return type(self)(
            code=alter1(code, self.code),
            description=alter1(description, self.description),
        )


class APIError(Exception):
    request: Request

    def __init__(self, request: Request, details: ErrorDetails) -> None:
        self.request = request
        self.details = details

        super().__init__(f"Telegram API returned an error: {details.description} (code {details.code})")


__all__ = ["ErrorDetails", "APIError"]

