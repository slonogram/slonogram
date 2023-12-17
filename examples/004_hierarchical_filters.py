from slonogram import Dispatcher, Ic, HandlerMarker, Context
from slonogram.schemas import Message

from utils import run_dispatcher

GRANT_TO_USERNAME = "s".casefold()
marker = HandlerMarker()


@marker.command("public")
async def public(ctx: Context[Message]) -> None:
    await ctx.reply("Public interface, wow!")


@marker.command("private")
async def private(ctx: Context[Message]) -> None:
    await ctx.reply("First private interface")


@marker.command("secret_information")
async def secret_information(ctx: Context[Message]) -> None:
    await ctx.reply(f"@{GRANT_TO_USERNAME}, you're the chosen one!")


def create_dispatcher() -> Dispatcher:
    return (
        Dispatcher("hierarchical_filters")
        .on(Ic.message, public)
        .child(
            Dispatcher("top_secret")
            .on(Ic.message, private)
            .on(Ic.message, secret_information)
            .filter(
                lambda ctx: ctx.model.from_.username.casefold() == GRANT_TO_USERNAME
            )
        )
    )


run_dispatcher(create_dispatcher())
