from slonogram import Dispatcher, Ic, Context
from slonogram.schemas import Message
from slonogram.filtering import Regex

from utils import run_dispatcher

BOT_NAME = r"(maid|м[эе][ий]да)"


async def call_response(ctx: Context[Message]) -> None:
    await ctx.reply("Did you called me?")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("regex_filter")
            .on(Ic.message, call_response, filter=Regex.contains(BOT_NAME))
    )
    # fmt: on


run_dispatcher(create_dispatcher())
