from utils import run_dispatcher

from slonogram import Dispatcher, Ic, Context
from slonogram.filtering import Command

from slonogram.schemas import InlineKeyboardMarkup, InlineKeyboardButton
from slonogram.schemas import Message, CallbackQuery


async def notify(ctx: Context[CallbackQuery]) -> None:
    await ctx.notify(text="You got a notification")


async def alert(ctx: Context[CallbackQuery]) -> None:
    await ctx.alert(text="You got an alert")


async def start(ctx: Context[Message]) -> None:
    await ctx.reply(
        "Select one of the options",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Get a notification", callback_data="notify"
                    )
                ],
                [InlineKeyboardButton(text="Get an alert", callback_data="alert")],
                [
                    InlineKeyboardButton(
                        text="Open project home page",
                        url="https://github.com/slonogram/slonogram",
                    )
                ],
            ]
        ),
    )


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("basic_callback")
            .on(Ic.message, start, filter=Command("start"))
            .on(Ic.callback_query, alert, filter=lambda x: x.model.data == "alert")
            .on(Ic.callback_query, notify, filter=lambda x: x.model.data == "notify")
    )
    # fmt: on


run_dispatcher(create_dispatcher())
