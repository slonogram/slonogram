from typing import TypeVar

from slonogram import Dispatcher, Ic, HandlerMarker, Context
from slonogram.schemas import Message, User

from slonogram.fsm import MemoryStorage
from slonogram.types.fsm import UserScope
from slonogram.abstract.fsm import FSMStorage
from slonogram.dispatching.stash import Stash

from utils import run_dispatcher

marker = HandlerMarker()

T = TypeVar("T")


def create_scope(from_: User | None) -> UserScope:
    if from_ is None:
        raise ValueError("There's no user")
    return UserScope(from_.id)


@marker.command()
async def grant_me_access(ctx: Context[Message]) -> None:
    await ctx.reply("Now you can access the /protected command!")
    await ctx.fsm_storage.write(create_scope(ctx.model.from_), True)


@marker.command()
async def protected(ctx: Context[Message]) -> None:
    storage = ctx.fsm_storage
    scope = create_scope(ctx.model.from_)

    if await storage.read(scope, bool, init_with=lambda: False):
        await ctx.reply("How did you get here? Get outta here")
        await storage.write(scope, False)
    else:
        await ctx.reply("You can't do this")


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("primitive_fsm")
            .on(Ic.message, protected)
            .on(Ic.message, grant_me_access)
            .with_stash(Stash.single(FSMStorage, MemoryStorage()))
    )
    # fmt: on


run_dispatcher(create_dispatcher())
