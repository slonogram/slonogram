import re

from typing import Iterable, Callable, TypeAlias, Optional

from slonogram.types.filter import ExtendedFilter
from slonogram.types.context import Context

from slonogram.extra.scratches import Text
from slonogram.schemas import Message, User

UsernamePredicate: TypeAlias = Callable[[User, str], bool]


def same_username(user: User, given: str) -> bool:
    return user.username == given


class Command(ExtendedFilter[Message]):
    __slots__ = "variants", "ignore_case", "pattern", "username_predicate"

    def __init__(
        self,
        variants: Iterable[str],
        ignore_case: bool = True,
        username_predicate: Optional[UsernamePredicate] = None,
    ) -> None:
        if isinstance(variants, str):
            variants = (variants,)
        if ignore_case:
            variants = map(str.casefold, variants)

        self.variants = tuple(variants)
        self.ignore_case = ignore_case
        self.pattern = re.compile(
            r"\/([\w\d_\-]+)(@([\w\d_]+))?",
            re.IGNORECASE if ignore_case else 0,
        )
        self.username_predicate = username_predicate or same_username

    def __repr__(self) -> str:
        return f"Command({self.variants!r})"

    async def __call__(self, ctx: Context[Message]) -> bool:
        text = ctx.pad[Text]
        if text is None:
            return False

        command_match = self.pattern.match(text)
        if command_match is None:
            return False

        command = command_match.group(1)
        if self.ignore_case:
            command = command.casefold()

        if command not in self.variants:
            return False

        username = command_match.group(3)
        if username is not None and not self.username_predicate(
            ctx.inter.me, username
        ):
            return False

        ctx.pad[Text] = text[command_match.end(0) :].lstrip()  # type: ignore

        return True


__all__ = ["same_username", "Command"]
