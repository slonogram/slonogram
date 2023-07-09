import asyncio

from slonogram import Bot

from slonogram.schemas import Message
from slonogram.dispatching import Dispatcher, LocalSet

from slonogram.filtering.text import Command

TOKEN = open(".test_token").read()

set_ = LocalSet()


@set_.on_message.sent(Command("start"))
async def start(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(
        message.chat.id, "Hello! I'll repeat everything you edit"
    )


@set_.on_message.edited()
async def edit_callback(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(
        message.chat.id, f"Edited: {message.text}", reply_to=message.id
    )


async def main() -> None:
    async with Bot(TOKEN) as bot:
        dp = Dispatcher(bot)
        dp.set.include(set_)

        await dp.run_polling()


asyncio.run(main())
