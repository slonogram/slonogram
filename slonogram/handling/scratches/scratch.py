from typing import TypeVar, TypeAlias, Callable

T = TypeVar("T")
R = TypeVar("R")

Scratch: TypeAlias = Callable[[T], R]


def attr_scratch(attr: str) -> Scratch[T, R]:
    class Impl:
        def __repr__(self) -> str:
            return f"<Scratch attr={attr!r}>"

        def __call__(self, model: T) -> R:
            return getattr(model, attr)

    return Impl()
