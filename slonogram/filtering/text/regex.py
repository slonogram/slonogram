from __future__ import annotations

import re

from typing import TYPE_CHECKING, TypeAlias
from enum import IntEnum, auto

if TYPE_CHECKING:
    from slonogram.dispatching.context import Context

from slonogram.schemas import Message
from ..base import ExtendedFilter

# fmt: off
class MatchMode(IntEnum):
    PREFIX    = auto()
    SUFFIX    = auto()
    FULL_MATCH = auto()
    CONTAINS  = auto()
# fmt: on

_Pattern: TypeAlias = str | re.Pattern[str]


class Regex(ExtendedFilter[Message]):
    __slots__ = (
        "pattern",
        "mode",
    )

    def __init__(
        self,
        pattern: _Pattern,
        *,
        flags: re.RegexFlag | None = None,
        mode: MatchMode = MatchMode.CONTAINS,
    ) -> None:
        if isinstance(pattern, re.Pattern):
            self.pattern = pattern
        else:
            self.pattern = re.compile(pattern, flags or re.IGNORECASE)

        self.mode = mode

    @classmethod
    def contains(
        cls,
        pattern: _Pattern,
        *,
        flags: re.RegexFlag | None = None,
    ) -> Regex:
        return cls(pattern, flags=flags, mode=MatchMode.CONTAINS)

    @classmethod
    def full_match(
        cls,
        pattern: _Pattern,
        *,
        flags: re.RegexFlag | None = None,
    ) -> Regex:
        return cls(pattern, flags=flags, mode=MatchMode.FULL_MATCH)

    @classmethod
    def suffix(
        cls,
        pattern: _Pattern,
        *,
        flags: re.RegexFlag | None = None,
    ) -> Regex:
        return cls(pattern, flags=flags, mode=MatchMode.SUFFIX)

    @classmethod
    def prefix(
        cls,
        pattern: _Pattern,
        *,
        flags: re.RegexFlag | None = None,
    ) -> Regex:
        return cls(pattern, flags=flags, mode=MatchMode.PREFIX)

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
        elif self.mode == MatchMode.FULL_MATCH:
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
