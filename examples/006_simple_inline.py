from slonogram import Dispatcher, Ic, Context
from slonogram.schemas import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from utils import run_dispatcher


async def inline(ctx: Context[InlineQuery]) -> None:
    await ctx.answer_inline(
        [
            InlineQueryResultArticle(
                id="1",
                title="First article",
                description=f"You entered {ctx.model.query}",
                input_message_content=InputTextMessageContent(message_text="Hello"),
            ),
        ]
    )


def create_dispatcher() -> Dispatcher:
    # fmt: off
    return (
        Dispatcher("simple_inline")
            .on(Ic.inline_query, inline)
    )
    # fmt: on


run_dispatcher(create_dispatcher())
