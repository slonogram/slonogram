import asyncio
from .base import run_bot

from slonogram import Bot, LocalSet
from slonogram.schemas import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

set_ = LocalSet()


@set_.on_inline()
async def respond_inline(bot: Bot, query: InlineQuery) -> None:
    print(
        await bot.query.answer_inline(
            query.id,
            [
                InlineQueryResultArticle(
                    "article",
                    "1",
                    "Hello",
                    InputTextMessageContent("Hello world"),
                )
            ],
        )
    )


asyncio.run(run_bot(set_))
