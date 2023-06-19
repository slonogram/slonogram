import asyncio

from typing import Any
from slonogram.dp import Dispatcher
from slonogram.dp.local_set import LocalSet
from slonogram.bot import Bot

set_ = LocalSet[Any]("test")


@set_.on_message.sent()
async def only_bot(bot: Bot) -> None:
    pass


async def main() -> None:
    async with Bot(open(".test_token").read()) as bot:
        dp = Dispatcher(bot)
        await dp.run_polling()


asyncio.run(main())
