from typing import Awaitable, Any

from ..session import extend_session
from ..types.request import Request

def _stub(
    req: Request,
    /
) -> Awaitable[Any]:
    _ = req
    raise NotImplementedError("Called stub")

stub = extend_session(_stub)

__all__ = ["stub"]
