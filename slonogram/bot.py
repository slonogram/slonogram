from adaptix import Retort, name_mapping

from typing import TypeVar, Optional, Callable

from .schemas.result import Result
from .protocols.session import Session
from .consts import TELEGRAM_API_URL

T = TypeVar("T")


class Bot:
    def __init__(
        self,
        token: str,
        api_url: str = TELEGRAM_API_URL,
        session_creator: Optional[
            Callable[[Retort, str, str], Session]
        ] = None,
    ) -> None:
        api_url = api_url.format(token=token, method="{method}")
        retort = Retort(
            debug_path=True,
            recipe=[
                name_mapping(Result, map={"data": "result"}),
                name_mapping(trim_trailing_underscore=True),
            ],
        )

        if session_creator is None:
            from .impls.aiohttp_session import AiohttpSession

            session: Session = AiohttpSession(retort, token, api_url)
        else:
            session = session_creator(retort, token, api_url)

        self._session = session

    @property
    def raw_session(self) -> Session:
        return self._session
