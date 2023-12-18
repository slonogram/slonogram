from typing import NewType

from slonogram import Dispatcher, Ic, Context, HandlerMarker
from slonogram.dispatching.stash import Stash
from slonogram.exceptions.stash import NoItemInStash
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


@marker.command("try")
async def have_no_access(ctx: Context[Message]) -> None:
    try:
        await ctx.reply("My name is %s" % ctx.stash[BotName])
    except NoItemInStash:
        await ctx.reply("Wow, I don't have access to my name, who am I?")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("hierarchical_stash")
            .with_stash(Stash.single(BotName, BotName("Medusa Maid")))
            .on(Ic.message, start)
            .child(
                Dispatcher()
                    .on(Ic.message, show_me)
            )
            .child(
                Dispatcher()
                    .on(Ic.message, have_no_access),
                relation=None
            )
    )
    # fmt: on


run_dispatcher(create_dispatcher())
