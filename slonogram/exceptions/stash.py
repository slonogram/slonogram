from typing import Type, Any


class CantReplaceStash(Exception):
    def __init__(self) -> None:
        super().__init__(
            "Can't replace dispatcher's stash because dispatcher have children"
        )


class NoItemInStash(Exception):
    __slots__ = ("type",)

    def __init__(self, type: Type[Any]) -> None:
        super().__init__(f"Could not find type {type} in the stash")

        self.type = type
