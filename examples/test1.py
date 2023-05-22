from slonogram.bot import Bot
from slonogram.dispatcher import Dispatcher

from asyncio import run

TOKEN = "token"


async def main() -> None:
    async with Bot(TOKEN) as bot:
        dp = Dispatcher(bot)
        await dp.run_polling()


run(main())
