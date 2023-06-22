import asyncio

from slonogram.bot import Bot

from slonogram.filters.text import Prefix, Eq

from slonogram.dp import Dispatcher
from slonogram.dp.local_set import LocalSet

from slonogram.schemas.chat import Message

local_set = LocalSet[None]("test")
prefix = Prefix(r"(м[еэ]йда?|maid)\s*")


@local_set.on_message.sent(prefix & Eq("мир"))
async def on_prefix(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "Hello world")


@local_set.on_message.edited(Eq("сыр"))
async def on_edited(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "Сыр")


@local_set.on_message.sent(prefix & Eq("ладность"))
async def on_ladno(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(message.chat.id, "Прохладность")


async def main() -> None:
    async with Bot(open(".test_token").read()) as bot:
        dp = Dispatcher(None, bot)
        dp.set.include(local_set)

        await dp.run_polling()


asyncio.run(main())
