import asyncio

from .base import run_bot

from slonogram import Bot, LocalSet
from slonogram.filtering.text import Command

from slonogram.schemas import (
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


TOKEN = open(".test_token").read()
set_ = LocalSet()


@set_.on_callback()
async def react_callback(bot: Bot, callback: CallbackQuery) -> None:
    if callback.data == "alert":
        await bot.query.answer_callback(
            callback.id, "Here's your alert, sir", show_alert=True
        )
    else:
        await bot.query.answer_callback(
            callback.id, "Here's your notification, sir"
        )


@set_.on_message.sent(Command("callback"))
async def callback_request(bot: Bot, message: Message) -> None:
    await bot.chat.send_message(
        message.chat.id,
        "Here's your buttons",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton("Alert", callback_data="alert"),
                    InlineKeyboardButton(
                        "Message", callback_data="message"
                    ),
                ]
            ]
        ),
    )


asyncio.run(run_bot(set_))
