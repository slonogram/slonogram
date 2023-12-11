import asyncio
import os

from slonogram.extra.session.aiohttp import create_session
from slonogram.bot import Bot


async def main() -> None:
    async with create_session(os.environ["BOT_TOKEN"]) as session:
        bot = Bot.from_session(session)


asyncio.run(main())
