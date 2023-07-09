from typing import Iterable

from slonogram.types.filter import ExtendedFilter
from slonogram.types.context import Context

from slonogram.extra.scratches import Text
from slonogram.schemas import Message

import re


class Word(ExtendedFilter[Message]):
    __slots__ = "pattern", "ignore_case"

    def __init__(
        self,
        variants: Iterable[str],
        regex: bool = False,
        ignore_case: bool = True,
    ) -> None:
        if isinstance(variants, str):
            variants = (variants,)
        if ignore_case:
            variants = map(str.casefold, variants)
        if not regex:
            variants = map(re.escape, variants)

        self.pattern = re.compile(
            "(" + "|".join(variants) + ")",
            re.IGNORECASE if ignore_case else 0,
        )
        self.ignore_case = ignore_case

    def __repr__(self) -> str:
        i = "i" if self.ignore_case else ""
        return f"Word({i}/{self.pattern.pattern}/)"

    async def __call__(self, ctx: Context[Message]) -> bool:
        text = ctx.pad[Text]
        if not text:
            return False

        space_pos = text.find(" ")
        if space_pos == -1:
            found_word = text
        else:
            found_word = text[:space_pos]

        if match := self.pattern.fullmatch(found_word):
            ctx.pad[Text] = text[match.end() :].lstrip()  # type: ignore
            return True
        return False
