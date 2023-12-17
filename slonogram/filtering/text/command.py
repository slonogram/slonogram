from __future__ import annotations
from typing import TYPE_CHECKING

from slonogram.utils import extract_from_utf16

if TYPE_CHECKING:
    from slonogram.dispatching.context import Context

from slonogram.schemas import Message
from slonogram.filtering.base import ExtendedFilter


class Command(ExtendedFilter[Message]):
    """A Telegram command. It simply parses commands from the message's entities,
    no custom logic available. To make your own command format consider creating your own filter.

    ## Text state awareness

    This filter is half-aware of the text state: it uses original message's text, but sets state
    to the text after the command

    :param variants: which commands to accept
    :type variants: tuple[str, ...]
    """

    __slots__ = ("variants",)

    def __init__(
        self,
        *variants: str,
    ) -> None:
        self.variants = tuple(map(str.casefold, variants))

    def __repr__(self) -> str:
        return f"Command<one_of={self.variants!r}>"

    def __call__(self, ctx: Context[Message]) -> bool:
        entities = ctx.model.entities
        text = ctx.model.text
        if not (entities and text):
            return False

        for entity in filter(
            lambda ent: ent.offset == 0 and ent.type == "bot_command",
            entities,
        ):
            command = extract_from_utf16(text, 1, entity.length - 1)
            offset = len(command) + 1
            command = command.casefold()

            if (at := command.find("@")) != -1:
                # Nested because of readability
                if ctx.rpc.username.casefold() != command[at + 1 :]:
                    return False
                command = command[:at]

            if command in self.variants:
                ctx.set_text(text[offset:].lstrip())
                return True

            return False

        return False


__all__ = ["Command"]
