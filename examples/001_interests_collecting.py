from slonogram import (
    Dispatcher,
    Context,
    Handler,     # for middlewares
    Activation,  # for middlewares
    ExtendedHandler,
    handler_from_compatible,
)
from slonogram.schemas import (
    Update,
    Message,
    CallbackQuery,
    InlineQuery,
)

# for .catch
from slonogram.types.caught_exception import CaughtException

@handler_from_compatible
async def test_msg(ctx: Context[Message]) -> None:
    print("Message")

@handler_from_compatible
async def test_callback(ctx: Context[CallbackQuery]) -> None:
    print("Callback")

@handler_from_compatible
async def test_inline(ctx: Context[InlineQuery]) -> None:
    print("Inline")

def introduce_message() -> Dispatcher[Update]:
    return Dispatcher().interested(message=test_msg)

def introduce_callback() -> Dispatcher[Update]:
    return Dispatcher().interested(callback_query=test_callback)

def introduce_inline() -> Dispatcher[Update]:
    return Dispatcher().interested(inline_query=test_inline)

async def do_nothing(ctx: Context[Update], next: Handler[Update]) -> Activation:
    return await next(ctx)

@handler_from_compatible
async def log_exception(ctx: Context[CaughtException[Update, SyntaxError]]) -> None:
    print(f'Caught exception {ctx.model.exc} while dispatching {ctx.model.model}')

def create_dispatcher() -> ExtendedHandler[Update]:
    return (
        Dispatcher[Update]()
            .register(introduce_message())
            .register(introduce_callback())
            .register(introduce_inline())
        
        .after(lambda ctx, next: next(ctx))
        .catch(SyntaxError, log_exception)
    )

dp = create_dispatcher()
print("Dispatcher =", dp)
print("Interests of dispatcher =", dp.collect_interests())


