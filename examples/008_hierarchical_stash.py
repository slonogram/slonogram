from typing import NewType

from slonogram import Dispatcher, Ic, Context, HandlerMarker
from slonogram.dispatching.stash import Stash
from slonogram.schemas import Message

from utils import run_dispatcher

BotName = NewType("BotName", str)
marker = HandlerMarker()


@marker.command()
async def start(ctx: Context[Message]) -> None:
    await ctx.reply(
        "Hey! I'm an 008_hierarchical_stash example. Call /show_me to proceed."
    )


@marker.command()
async def show_me(ctx: Context[Message]) -> None:
    await ctx.reply("My name is %s" % ctx.stash[BotName])


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("hierarchical_stash")
            .on(Ic.message, start)
            .child(
                Dispatcher()
                    .on(Ic.message, show_me)
            )
            .with_stash(Stash.single(BotName, BotName("Medusa Maid")))
    )
    # fmt: on


run_dispatcher(create_dispatcher())
