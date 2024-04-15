from typing import Awaitable, Any, assert_type

from ..abstract.session import Session
from ..types.request import Request

def stub(
    req: Request,
    /
) -> Awaitable[Any]:
    _ = req
    raise NotImplementedError("Called stub")


assert_type(stub, Session)

__all__ = ["stub"]
