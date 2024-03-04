from typing import Protocol, TypeVar

Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output")

class Stage(Protocol[Input, Output]):
    def write(self, value: Output) -> str:
        ...

    def create_specification(self, args: Input) -> Output:
        ...


__all__ = ["Stage"]
