from slonogram.dispatching import Dispatcher, Context
from slonogram.schemas import Message, CallbackQuery

from slonogram.dispatching import interests as I


async def test(ctx: Context[Message]) -> None:
    print("Message!")


async def callback(ctx: Context[CallbackQuery]) -> None:
    print("Callback")


async def multi_model(ctx: Context[CallbackQuery | Message]) -> None:
    print("Variance!")


def true(ctx: Context[Message]) -> bool:
    return True


# fmt: off
dp = (
    Dispatcher()
        .register(I.message > test)
        .register(I.message > test, filter=true)
        .register(I.message | I.edited_message > test)
        .register(I.callback_query > callback)
        .register(
            I.callback_query_r
            | I.inline_query_r
            | I.message_r
            > multi_model
        )

)
# fmt: on
