import re
from typing import Any, Set, List, Tuple

from .extended import ExtendedFilter

from ..dp.context import Context
from ..handling.scratches import Text
from ..schemas.chat import Message
from ..consts import COMMAND_REGEX


class Command(ExtendedFilter[Any, Message]):
    def __init__(
        self,
        variants: str | Set[str] | List[str] | Tuple[str],
        regex: str = COMMAND_REGEX,
        case_sensitive: bool = False,
    ) -> None:
        variants = (variants,) if isinstance(variants, str) else variants
        if not case_sensitive:
            variants = type(variants)(
                v.casefold() for v in variants
            )  # type:ignore
        self.variants = variants
        self.pattern = re.compile(
            regex, 0 if case_sensitive else re.IGNORECASE
        )

        self.case_sensitive = case_sensitive

    async def __call__(self, ctx: Context[Any, Message]) -> bool:
        text = ctx.pad.get(Text)
        if text is None:
            return False

        match = self.pattern.match(text)
        if match is None:
            return False

        command = match.group(1)
        user = match.group(3)

        if not self.case_sensitive:
            command = command.casefold()

        if user is not None and user != ctx.inter.me.username:
            return False

        if command not in self.variants:
            return False

        end = match.end(0)
        ctx.pad.scratch(Text, text[end:].lstrip())  # type: ignore
        return True
