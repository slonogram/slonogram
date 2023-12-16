from __future__ import annotations

import re

from typing import TYPE_CHECKING
from enum import IntEnum, auto

if TYPE_CHECKING:
    from slonogram.dispatching.context import Context

from slonogram.schemas import Message
from ..base import ExtendedFilter

# fmt: off
class MatchMode(IntEnum):
    PREFIX    = auto()
    SUFFIX    = auto()
    FULLMATCH = auto()
    CONTAINS  = auto()
# fmt: on


class Regex(ExtendedFilter[Message]):
    __slots__ = (
        "pattern",
        "mode",
    )

    def __init__(
        self,
        pattern: str | re.Pattern,
        *,
        flags: re.RegexFlag = re.IGNORECASE,
        mode: MatchMode = MatchMode.CONTAINS,
    ) -> None:
        if isinstance(pattern, re.Pattern):
            self.pattern = pattern
        else:
            self.pattern = re.compile(pattern, flags)

        self.mode = mode

    def __repr__(self) -> str:
        return f"r/{self.pattern.pattern}/"

    def __call__(self, ctx: Context[Message]) -> bool:
        text = ctx.grasp_text()
        if text is None:
            return False

        if self.mode == MatchMode.PREFIX:
            match = self.pattern.match(text)
            if match is None:
                return False

            ctx.set_text(text[match.end() :])
        elif self.mode == MatchMode.FULLMATCH:
            return self.pattern.fullmatch(text) is not None
        elif self.mode == MatchMode.SUFFIX:
            match = self.pattern.search(text + "$")
            if match is None:
                return False

            ctx.set_text(text[: match.start()])
        elif self.mode == MatchMode.CONTAINS:
            return self.pattern.search(text) is not None

        return True


__all__ = ["Regex", "MatchMode"]
