from typing import Awaitable
from anyio import sleep

from .extended import ExtendedMiddleware

from ..exceptions.api import ApiError
from ..utils.typing import MaybeException

from ..session import Session
from ..session.gate import MethodCall

RATE_LIMITED = 429


async def _none() -> None:
    pass


class BackoffRetry(ExtendedMiddleware[[Session, MethodCall, MaybeException], None]):
    __slots__ = (
        "factor",
        "max_retries",
        "first_wait",
    )

    def __init__(
        self,
        factor: float = 1.5,
        *,
        max_retries: int = 5,
        first_wait: float = 1.0,
    ) -> None:
        self.factor = factor
        self.max_retries = max_retries
        self.first_wait = first_wait

    def __repr__(self) -> str:
        return f"BackoffRetry({self.first_wait} * {self.factor}^N)"

    async def _enter_backoff(
        self,
        session: Session,
        call: MethodCall,
    ) -> None:
        call_method = session.gate.call_method
        retries = 0
        wait = self.first_wait

        while retries < self.max_retries:
            try:
                call.response = await call_method(call)
                return
            except ApiError as exc:
                if exc.details.code == RATE_LIMITED:
                    retries += 1

                    await sleep(wait)
                    wait *= self.factor
                    continue
                raise

        raise

    def __call__(
        self,
        session: Session,
        call: MethodCall,
        exc: MaybeException,
    ) -> Awaitable[None]:
        if exc is not None:
            if isinstance(exc, ApiError) and exc.details.code == RATE_LIMITED:
                return self._enter_backoff(session, call)
            raise

        return _none()


__all__ = ["BackoffRetry"]
