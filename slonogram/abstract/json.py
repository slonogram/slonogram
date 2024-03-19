from typing import Protocol, Any


class JSONParser(Protocol):
    def __call__(self, data: bytes, /) -> Any:
        ...

class JSONDumper(Protocol):
    def __call__(self, data: Any, /) -> str:
        ...


__all__ = ["JSONParser", "JSONDumper"]
