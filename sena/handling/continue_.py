import typing as t

from ..control_flow import Continue

C = t.TypeVar("C")

async def continue_(req: C) -> Continue[C]:
    return Continue(req)


__all__ = ["continue_"]

