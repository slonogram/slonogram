from typing import Any

from slonogram.dispatching import Activation
from slonogram.dispatching.handler import RawHandler


def assert_activation(raw: RawHandler[Any] | None, result: Activation[Any]) -> None:
    if raw is None:
        assert not result.is_activated
    else:
        assert result.handler is not None and result.handler.raw == raw


__all__ = ["assert_activation"]
