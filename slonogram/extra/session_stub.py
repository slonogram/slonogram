from typing import Awaitable, Any, assert_type
from ..abstract.session import Session, Params, FilesMap


def stub(
    name: str,
    params: Params,
    files: FilesMap,
    /
) -> Awaitable[Any]:
    raise NotImplementedError("Called stub")


assert_type(stub, Session)

__all__ = ["stub"]
