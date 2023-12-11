from slonogram.dispatching import (
    Dispatcher,
    Context,
    interests as Ic,
)
from slonogram.schemas import Message, CallbackQuery, InlineQuery


async def message(ctx: Context[Message]) -> None:
    ...


async def callback(ctx: Context[CallbackQuery]) -> None:
    ...


async def inline(ctx: Context[InlineQuery]) -> None:
    ...


def t(t: Context[Message]) -> bool:
    return True


# fmt: off
dp = (
    Dispatcher("main")
        .on(Ic.message > message)
        .filter(lambda ctx: ctx.model.chat.id == 10)
)
# fmt: on
