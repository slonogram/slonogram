from typing import Protocol, TypeAlias, BinaryIO, Any, Awaitable

Scalar: TypeAlias = str
Key: TypeAlias = str

Params: TypeAlias = dict[Key, Scalar]
FilesMap: TypeAlias = dict[Key, BinaryIO]

class Session(Protocol):
    def __call__(
        self,
        name: str,
        params: Params,
        files: FilesMap,
        /,
    ) -> Awaitable[Any]:
        ...


__all__ = [
    "Session",
    "Params",
    "FilesMap",
]
