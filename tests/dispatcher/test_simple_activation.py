import pytest

from test_helpers.message import MESSAGE_MOCK
from test_helpers import BOT_MOCK
from test_helpers.update import update


from typing import Any

from slonogram import schemas
from slonogram.filtering import Const, BareFilter

from slonogram.dispatching import (
    Dispatcher,
    HandlerActivation,
    Context,
    Ic,
)
from slonogram.dispatching.interests import Interested

pytest_plugins = ("pytest_asyncio",)

dp = Dispatcher("test_simple_activation")


async def _stub(_: Context[Any]) -> None:
    ...


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "filter,finalized,expect",
    [
        (Const(True), Ic.message > _stub, HandlerActivation.activated),
        (Const(False), Ic.message > _stub, HandlerActivation.ignored),
        (Const(True), Ic.edited_message > _stub, HandlerActivation.ignored),
        (
            Const(True),
            Ic.message | Ic.edited_message > _stub,
            HandlerActivation.activated,
        ),
    ],
)
async def test_activation(
    filter: BareFilter[Any],
    finalized: Interested[Any, Any],
    expect: HandlerActivation,
) -> None:
    assert (
        await dp.on(finalized, filter=filter).feed_single(
            schemas.Update(update_id=1337, message=MESSAGE_MOCK),
            BOT_MOCK,
        )
    ) == expect


MSG_UPD = update(message=MESSAGE_MOCK)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "test_dp,input,expect",
    [
        (dp.on(Ic.message > _stub), MSG_UPD, HandlerActivation.activated),
        (dp.on(Ic.callback_query > _stub), MSG_UPD, HandlerActivation.ignored),
        (
            dp.on(Ic.message | Ic.edited_message > _stub).on(Ic.callback_query > _stub),
            MSG_UPD,
            HandlerActivation.activated,
        ),
    ],
)
async def test_multiple_activations(
    test_dp: Dispatcher,
    input: schemas.Update,
    expect: HandlerActivation,
) -> None:
    assert (await test_dp.feed_single(input, BOT_MOCK)) == expect
