from typing import NewType, Awaitable, TypeVar

from slonogram import Dispatcher, Ic, Context
from slonogram.schemas import Message

from slonogram.dispatching.stash import Stash
from slonogram.dispatching.handler import RawHandler
from slonogram.dispatching.marker import GenericMarker, GenericRawHandler

from utils import run_dispatcher

M = TypeVar("M")
BotName = NewType("BotName", str)


def morph(g: GenericRawHandler[M, [BotName], Awaitable[None]]) -> RawHandler[M]:
    return lambda ctx: g(ctx, ctx.stash[BotName])


marker = GenericMarker(morph)


@marker.command()
async def start(ctx: Context[Message], name: BotName) -> None:
    await ctx.reply(f"My name is {name}")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("generic_marker")
            .with_stash(Stash.single(BotName, BotName("Maid")))
            .on(Ic.message, start)
    )
    # fmt: on


run_dispatcher(create_dispatcher())
