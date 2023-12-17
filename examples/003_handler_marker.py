from slonogram import HandlerMarker, Dispatcher, Ic, Context
from slonogram.schemas import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from utils import run_dispatcher

marker = HandlerMarker()


@marker(filter=lambda ctx: ctx.model.data == "marker")
async def show_alert(context: Context[CallbackQuery]) -> None:
    await context.alert(text="Marker works!")


@marker.command("start")
async def start(context: Context[Message]) -> None:
    await context.reply(
        "Select the button",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton("Click me!", callback_data="marker")],
            ]
        ),
    )


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("handler_marker")
            .on(Ic.callback_query, show_alert)
            .on(Ic.message, start)
    )
    # fmt: on


run_dispatcher(create_dispatcher())
