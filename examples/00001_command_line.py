import asyncio

from traceback import print_exception
from dataclasses import dataclass

from slonogram.extra.session_stub import stub
from slonogram.exceptions.stash import CannotProvideError
from slonogram.filtering import Filter
from slonogram import (
    Context,
    activate,
    Handler,
    Activation,
    Dispatcher,
    Bot,
    Stash,
)


@dataclass(slots=True)
class TextPosition:
    pos: int


def get_text(stash: Stash, model: str) -> str:
    return model[stash[TextPosition].pos :]


def offset_text(stash: Stash, acc: int) -> None:
    try:
        stash[TextPosition].pos += acc
    except CannotProvideError:
        stash[TextPosition] = TextPosition(acc)


async def help(ctx: Context[str]) -> None:
    print("# Help on available commands")
    print("  - help - show this message")
    print("  - say <anything> - prints something in the command prompt")
    print(
        "  - eval <expr> - evaluates python expression and prints result to the terminal"
    )


async def say(ctx: Context[str]) -> None:
    something = get_text(ctx.stash, ctx.model)
    print(f">> I say {something!r}!")


async def evaluate(ctx: Context[str]) -> None:
    expr_raw = get_text(ctx.stash, ctx.model)
    result = eval(expr_raw)

    print(">> Result is", result)


async def handle_exception(ctx: Context[str], next: Handler[str]) -> Activation:
    try:
        return await next(ctx)
    except Exception as exc:
        print(f"Encountered exception while evaluating: {exc}, details below")
        print_exception(None, exc, None)

        return Activation.stalled()


async def not_found(ctx: Context[str]) -> None:
    print("Command not found, enter `help` for help")


def word(w: str) -> Filter[str]:
    def inner(ctx: Context[str]) -> bool:
        space_pos = ctx.model.find(" ")
        if space_pos == -1:
            chk_str = ctx.model
            acc = len(chk_str)
        else:
            chk_str = ctx.model[:space_pos]
            acc = len(chk_str) + 1

        if chk_str == w:
            offset_text(ctx.stash, acc)
            return True
        return False

    return inner


async def main() -> None:
    bot = Bot(stub)
    stash = Stash()
    dp = (
        Dispatcher[str](name="CLI")
            .register(activate(help) & word("help"))
            .register(activate(say) & word("say"))
            .register(activate(evaluate) & word("eval"))
            .register(activate(not_found))
        << handle_exception
    )

    while True:
        command = input("command> ")
        await dp(Context(bot, command, stash))


asyncio.run(main())
