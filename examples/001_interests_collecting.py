from slonogram import Dispatcher, Context
from slonogram.schemas import Update, Message, CallbackQuery, InlineQuery

from slonogram.handling.compatible import handler_from_compatible

@handler_from_compatible
async def test_msg(ctx: Context[Message]) -> None:
    print("Message")

@handler_from_compatible
async def test_callback(ctx: Context[CallbackQuery]) -> None:
    print("Callback")

@handler_from_compatible
async def test_inline(ctx: Context[InlineQuery]) -> None:
    print("Inline")

def introduce_message() -> Dispatcher[Update]:
    return Dispatcher().interested(message=test_msg)

def introduce_callback() -> Dispatcher[Update]:
    return Dispatcher().interested(callback_query=test_callback)

def introduce_inline() -> Dispatcher[Update]:
    return Dispatcher().interested(inline_query=test_inline)

def create_dispatcher() -> Dispatcher[Update]:
    return (
        Dispatcher[Update]()
            .register(introduce_message())
            .register(introduce_callback())
            .register(introduce_inline())
    )

dp = create_dispatcher()
print("Dispatcher =", dp)
print("Interests of dispatcher =", dp.collect_interests())


