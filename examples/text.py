import asyncio

from slonogram.bot import Bot

from slonogram.dispatcher import Dispatcher
from slonogram.dispatcher.local_set import LocalSet

from slonogram.schemas.chat import Message
from slonogram.filtering.message import TextEq, TextContains

TOKEN = open(".test-token").read()

local_set = LocalSet("main")


@local_set.message.when(~TextEq("hello") & TextContains("llo"))
async def reply(bot: Bot, message: Message) -> None:
    print("Hello world")
    await bot.chat.send_message(message.chat.id, "Hello world!")


async def main() -> None:
    bot = Bot(TOKEN)
    dp = Dispatcher(bot)
    dp.register_set(local_set)

    await dp.run_polling()


asyncio.run(main())
