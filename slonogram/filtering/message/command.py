from slonogram.schemas.chat import Message
from ..chainable_filter import ChainableFilter


class Command(ChainableFilter):
    def __init__(self) -> None:
        pass

    def __call__(self, message: Message) -> Message:
        return message


def command() -> Command:
    return Command()


__all__ = ["Command", "command"]
