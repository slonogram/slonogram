import asyncio

from typing import NewType

from slonodi import Container
from slonodi.specifiers import requires

from slonogram.extra.aiohttp_session import Session
from slonogram.extra.scratches import Text
from slonogram.extra.di import (
    from_scratch,
    create_injector,
)

from slonogram.bot import Bot
from slonogram.schemas import Message
from slonogram.filtering.text import Command
from slonogram.dispatching import LocalSet, Dispatcher

TOKEN = open(".test_token").read()
Master = NewType("Master", str)

container = Container()
container[Master] = Master("Nero")

injector = create_injector()
inject = injector.inject


set_ = LocalSet()


@set_.on_message.sent(Command("get_master"))
@inject(from_scratch("text", Text), requires("master"))
async def on_get_master(
    bot: Bot, message: Message, text: str, master: Master
) -> None:
    await bot.chat.send_message(
        message.chat.id,
        f"My master is {master} (scratch text = {text})",
    )


async def main() -> None:
    async with Bot(Session(TOKEN)) as bot:
        dp = Dispatcher(bot)
        dp.data = container
        dp.set.include(set_)
        await dp.run_polling()


asyncio.run(main())
