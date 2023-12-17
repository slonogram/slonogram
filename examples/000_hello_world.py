import asyncio
from utils import run_dispatcher

from slonogram import Dispatcher, Context, Ic

from slonogram.schemas import Message
from slonogram.filtering import Command


async def start(ctx: Context[Message]) -> None:
    await ctx.reply("Hello world!")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher(__name__)
            .on(Ic.message, start, filter=Command("start"))
    )
    # fmt: on


run_dispatcher(create_dispatcher())
