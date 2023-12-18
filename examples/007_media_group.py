# THIS EXAMPLE DOES NOT WORK!

from slonogram import Dispatcher, Ic, Context, HandlerMarker
from slonogram.schemas import Message, InputMediaPhoto

from utils import run_dispatcher

marker = HandlerMarker()


@marker.command()
async def send_media(ctx: Context[Message]) -> None:
    await ctx.reply_media_group(
        [
            InputMediaPhoto(open("suiseiseki_small.jpeg", "rb")),
            InputMediaPhoto(open("suiseisekii.png", "rb")),
        ]
    )


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("media_group")
            .on(Ic.message, send_media)
    )
    # fmt: on


run_dispatcher(create_dispatcher())
