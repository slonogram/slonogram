from typing import TypeVar, Awaitable

from .context import AbstractContext

from ..schemas import Message

M = TypeVar("M")


class ShortcutsMixin(AbstractContext[M]):
    def reply(
        self: AbstractContext[Message],
        *args,
        **kwargs,
    ) -> Awaitable[Message]:
        """Same as calling `Bot.send_message` with a `context.model.chat.id`"""
        return self.rpc.send_message(self.model.chat.id, *args, **kwargs)
