from typing import (
    TypeVar,
    Callable,
    Concatenate,
    TypeAlias,
    Generic,
    Protocol,
    Awaitable,
    ParamSpec,
)

from ..filtering.base import BareFilter, ExtendedFilter
from ..filtering.text.command import Command

from ..schemas import Message

from .handler import Handler, RawHandler
from .context import Context, CtxMiddleware, CtxExcMiddleware
from .layers import Layers

T = TypeVar("T", contravariant=True)
M = TypeVar("M")
P = ParamSpec("P")


GenericRawHandler: TypeAlias = Callable[Concatenate[Context[M], P], T]
GenericHandlerDeco: TypeAlias = Callable[[GenericRawHandler[M, P, T]], Handler[M]]


class MorphMarker(Protocol[T, P]):
    def __call__(
        self,
        f: GenericRawHandler[M, P, T],
        /,
    ) -> RawHandler[M]:
        ...


class GenericMarker(Generic[T, P]):
    """Generic marker.

    Used to create instances of the :ref:`Handler[M]` from almost any function
    """

    def __init__(self, morph_marker: MorphMarker[T, P]) -> None:
        self.morph_marker = morph_marker

    def command(
        self,
        *variants: str,
        filter: BareFilter[Message] | None = None,
        prepare: CtxMiddleware[Message, []] | None = None,
        before: CtxMiddleware[Message, []] | None = None,
        after: CtxExcMiddleware[Message] | None = None,
    ) -> GenericHandlerDeco[Message, P, T]:
        if not variants:

            def parse_from_function_name(
                raw: GenericRawHandler[Message, P, T]
            ) -> Handler[Message]:
                name = getattr(raw, "__name__", None)
                if name is None:
                    raise TypeError(
                        "Calling command without variants only possible with functions "
                        "that have the `__name__` dunder"
                    )
                return self(
                    filter=Command(name),
                    prepare=prepare,
                    before=before,
                    after=after,
                )(raw)

            return parse_from_function_name

        assigned_filter: ExtendedFilter[Message] = Command(*variants)
        if filter is not None:
            assigned_filter &= filter

        return self(
            filter=assigned_filter,
            prepare=prepare,
            before=before,
            after=after,
        )

    def __call__(
        self,
        filter: BareFilter[M] | None = None,
        *,
        prepare: CtxMiddleware[M, []] | None = None,
        before: CtxMiddleware[M, []] | None = None,
        after: CtxExcMiddleware[M] | None = None,
    ) -> GenericHandlerDeco[M, P, T]:
        def _create(raw: GenericRawHandler[M, P, T]) -> Handler[M]:
            return Handler(
                self.morph_marker(raw),
                Layers(
                    prepare,
                    before,
                    after,
                    filter,
                ),
            )

        return _create


def _identity(c: GenericRawHandler[M, [], Awaitable[None]]) -> RawHandler[M]:
    return c


# Due to lack of something like
# impl GenericHandlerMarker[Awaitable[None], []]:
#     ...
#
# I'll use inheritance to give reasonable default (when no morphing is used)
class HandlerMarker(GenericMarker[Awaitable[None], []]):
    """:ref:`GenericMarker` specialization only for handlers without additional morphing"""

    def __init__(self) -> None:
        super().__init__(_identity)

    def __repr__(self) -> str:
        return "<Marker>"


__all__ = [
    "HandlerMarker",
    "MorphMarker",
    "GenericMarker",
    "GenericRawHandler",
    "GenericHandlerDeco",
]
