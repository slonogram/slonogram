from __future__ import annotations

from typing import (
    Protocol,
    Any,
    TypeVar,
    Callable,
    TypeAlias,
    overload,
)
from io import IOBase

from adaptix import Retort

from ..utils.typing import MaybeException
from ..utils.hof import Alter1, alter1, apply1

from .middleware import SessionMiddlewares, SessionMiddleware
from .gate import ApiGate, NO_RESPONSE, MethodCall


class CanCollectAttachs(Protocol):
    def collect_attachs(self, dest: dict[str, IOBase]) -> None:
        ...


def get_response(exc: MaybeException, call: MethodCall) -> Any:
    response = call.response
    if exc is not None and response is NO_RESPONSE:
        raise exc

    return response


T = TypeVar("T")


class Session:
    __slots__ = ("retort", "gate", "middlewares")

    def __init__(
        self,
        retort: Retort,
        gate: ApiGate,
        *,
        middlewares: SessionMiddlewares | None = None,
    ) -> None:
        self.retort = retort
        self.gate = gate

        if middlewares is None:
            middlewares = SessionMiddlewares()
        self.middlewares = middlewares

    def alter(
        self,
        *,
        middlewares: Alter1[SessionMiddlewares] | None = None,
        retort: Alter1[Retort] | None = None,
        gate: Alter1[ApiGate] | None = None,
    ) -> Session:
        return Session(
            retort=alter1(retort, self.retort),
            gate=alter1(gate, self.gate),
            middlewares=alter1(middlewares, self.middlewares),
        )

    async def call_method(
        self,
        name: str,
        args: T,
    ) -> Any:
        """Calls specified method of the telegram api

        :param name: name of the method
        :param args: Arguments for the method

        :raises: `slonogram.exceptions.api.ApiError` if call failed
        :return: Response of the telegram api, directly the `result` payload
        """
        dumped_args: dict[str, str] = self.retort.dump(args)
        files: dict[str, IOBase] = {}
        args.collect_attachs(files)  # type: ignore

        call = MethodCall(
            name,
            dumped_args,
            files,
            NO_RESPONSE,
        )
        middlewares = self.middlewares
        try:
            if middlewares.before is not None:
                await middlewares.before(self, call)
        except Exception as exc:
            if middlewares.after is not None:
                await middlewares.after(self, call, exc)
            return get_response(exc, call)

        try:
            result = await self.gate.call_method(call)
            call.response = result
        except Exception as exc:
            if middlewares.after is not None:
                await middlewares.after(self, call, exc)
            return get_response(exc, call)
        else:
            if middlewares.after is not None:
                await middlewares.after(self, call, None)

        return get_response(None, call)


_AddMiddleware: TypeAlias = Callable[[Session], Session]


def _middlewares_alterer(
    alter_with: SessionMiddlewares,
    middlewares: SessionMiddlewares,
) -> SessionMiddlewares:
    return middlewares & alter_with


def _create_mw_alterer(value: SessionMiddlewares) -> _AddMiddleware:
    def session_alterer(session: Session) -> Session:
        return session.alter(middlewares=apply1(_middlewares_alterer, value))

    return session_alterer


@overload
def add_middleware(
    *,
    before: SessionMiddleware[[]] | None = None,
    after: SessionMiddleware[[MaybeException]] | None = None,
) -> _AddMiddleware:
    ...


@overload
def add_middleware(middlewares: SessionMiddlewares) -> _AddMiddleware:
    ...


def add_middleware(
    middlewares: SessionMiddlewares | None = None,
    *,
    before: SessionMiddleware[[]] | None = None,
    after: SessionMiddleware[[MaybeException]] | None = None,
) -> _AddMiddleware:
    if middlewares is not None:
        return _create_mw_alterer(middlewares)
    return _create_mw_alterer(
        SessionMiddlewares(
            before=before,
            after=after,
        )
    )


__all__ = [
    "CanCollectAttachs",
    "Session",
    "add_middleware",
]
