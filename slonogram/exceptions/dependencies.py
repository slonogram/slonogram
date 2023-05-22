from typing import Generic, TypeVar
from inspect import Parameter

T = TypeVar("T")


class UnsupportedArgKindError(Exception):
    def __init__(self, fn_name: str, parameter: Parameter) -> None:
        self.fn_name = fn_name
        self.parameter = parameter

        super().__init__(
            f"unsupported argument kind "
            f"in function {fn_name}: {parameter.kind}"
        )


class DependencyIsAlreadyExistsError(Generic[T], Exception):
    def __init__(self, value: T) -> None:
        self.value = value

        super().__init__(
            f"dependency is already present in the container:"
            f" {type(value).__name__}"
        )
