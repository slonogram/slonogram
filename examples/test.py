import asyncio

from slonogram.dp.context import Context
from slonogram.dp import Dispatcher
from slonogram.dp.local_set import LocalSet
from slonogram.filters.types import FilterFn

from slonogram.schemas.chat import Message
from slonogram.bot import Bot
from slonogram.schemas.updates import UpdateType

local_set = LocalSet[None]("test")


def text_eq(text: str) -> FilterFn:
    async def filter_(context: Context[None, Message]) -> bool:
        return context.model.text == text

    return filter_


@local_set.on_message.edited(text_eq("/123"))
async def print_message(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "123")


async def main() -> None:
    async with Bot(open(".test_token").read()) as bot:
        dp = Dispatcher(None, bot)
        dp.set.include(local_set)

        await dp.run_polling(
            allowed_updates=[UpdateType.message, UpdateType.edited_message]
        )


asyncio.run(main())
