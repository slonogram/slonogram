from slonogram.types.filter import ExtendedFilter
from slonogram.types.context import Context
from slonogram.schemas import Message

from slonogram.extra.scratches import Text

import re


class Prefix(ExtendedFilter[Message]):
    __slots__ = "ignore_case", "pattern"

    def __init__(self, pattern: str, ignore_case: bool = True) -> None:
        self.pattern = re.compile(
            pattern, re.IGNORECASE if ignore_case else 0
        )
        self.ignore_case = ignore_case

    async def __call__(self, ctx: Context[Message]) -> bool:
        text = ctx.pad[Text]
        if text is None:
            return False

        match = self.pattern.match(text)
        if match is None:
            return False

        end = match.end(0)
        ctx.pad[Text] = text[end:]  # type: ignore

        return True
