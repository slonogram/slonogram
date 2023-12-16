import asyncio
import os

from slonogram.extra.session.aiohttp import create_session
from slonogram.executors.long_polling import poll_for_updates

from slonogram.dispatching import Dispatcher, Context, Ic
from slonogram.filtering.text import Regex

from slonogram.schemas import Message
from slonogram.bot import Bot


async def help(ctx: Context[Message]) -> None:
    await ctx.reply("There's no help... It's just an example")


async def edited(ctx: Context[Message]) -> None:
    await ctx.reply("I saw you edited something")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher(__name__)
            .on(Ic.message, help, filter=Regex(r"help\s*") & Regex(r"(me)?"))
            .on(Ic.edited_message, edited)
    )
    # fmt: on


async def main() -> None:
    async with create_session(os.environ["BOT_TOKEN"]) as session:
        bot = await Bot.from_session(session)
        await poll_for_updates(bot, create_dispatcher())


asyncio.run(main())
