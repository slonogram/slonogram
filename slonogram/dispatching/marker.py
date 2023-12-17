from typing import TypeVar, Callable, TypeAlias

from ..filtering.base import BareFilter, ExtendedFilter
from ..filtering.text.command import Command

from ..middleware import SimpleMiddleware, ExcMiddleware
from ..schemas import Message

from .handler import Handler, RawHandler
from .layers import Layers

M = TypeVar("M")
_HandlerDeco: TypeAlias = Callable[[RawHandler[M]], Handler[M]]


class HandlerMarker:
    def __repr__(self) -> str:
        return "<Marker>"

    def command(
        self,
        *variants: str,
        filter: BareFilter[Message] | None = None,
        prepare: SimpleMiddleware[Message] | None = None,
        before: SimpleMiddleware[Message] | None = None,
        after: ExcMiddleware[Message] | None = None,
    ) -> _HandlerDeco[Message]:
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
        prepare: SimpleMiddleware[M] | None = None,
        before: SimpleMiddleware[M] | None = None,
        after: ExcMiddleware[M] | None = None,
    ) -> _HandlerDeco[M]:
        def _create(raw: RawHandler[M]) -> Handler[M]:
            return Handler(
                raw,
                Layers(
                    prepare,
                    before,
                    after,
                    filter,
                ),
            )

        return _create
