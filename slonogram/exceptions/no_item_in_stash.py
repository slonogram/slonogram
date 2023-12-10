from typing import Type, Any


class NoItemInStash(Exception):
    __slots__ = ("type",)

    def __init__(self, type: Type[Any]) -> None:
        super().__init__(f"Could not find type {type} in the stash")

        self.type = type
