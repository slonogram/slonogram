from slonogram.dispatching import Dispatcher, Context
from slonogram.schemas import Message, CallbackQuery

from slonogram.dispatching.interests import (
    message,
    edited_message,
    callback_query,
)


async def test(ctx: Context[Message]) -> None:
    print("Message!")


async def callback(ctx: Context[CallbackQuery]) -> None:
    print("Callback")


def true(ctx: Context[Message]) -> bool:
    return True


# fmt: off
dp = (
    Dispatcher()
        .register(message > test)
        .register(message > test, filter=true)
        .register(message | edited_message > test)
        .register(callback_query > callback)
)
# fmt: on
