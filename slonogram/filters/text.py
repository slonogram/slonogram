import re

from typing import Any

from slonogram.dp.context import Context

from ..schemas.chat import Message
from ..handling.scratches import Text

from .extended import ExtendedFilter


# Some way to minimize this boilerplate?
class Eq(ExtendedFilter[Any, Message]):
    def __init__(self, text: str, case_sensitive: bool = False) -> None:
        self.case_sensitive = case_sensitive
        self.text = text if case_sensitive else text.casefold()

    async def __call__(self, ctx: Context[Any, Message]) -> bool:
        text = ctx.pad.get(Text)
        if text is None:
            return False

        if self.case_sensitive:
            return text == self.text
        return text.casefold() == self.text

    def __repr__(self) -> str:
        casefolding = "" if self.case_sensitive else ".casefold()"
        return f"(text{casefolding} == {self.text!r})"


class Prefix(ExtendedFilter[Any, Message]):
    def __init__(self, pattern: str, case_sensitive: bool = False) -> None:
        flags = 0 if case_sensitive else re.IGNORECASE
        self.pattern = re.compile(pattern, flags)

    def __repr__(self) -> str:
        ignorecase_sym = "i" if self.pattern.flags & re.IGNORECASE else ""
        return f"/{self.pattern.pattern}/{ignorecase_sym}"

    async def __call__(self, ctx: Context[Any, Message]) -> bool:
        text = ctx.pad.get(Text)
        if text is None:
            return False

        match = self.pattern.match(text)
        if match is None:
            return False
        end = match.end()

        ctx.pad.scratch(Text, text[end:])  # type: ignore
        return True
