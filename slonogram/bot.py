from adaptix import Retort, name_mapping

from typing import TypeVar, Optional, Callable, Self

from .schemas.result import Result
from .schemas.chat import Message
from .schemas.updates import Update

from .protocols.session import Session
from .consts import TELEGRAM_API_URL

from .wrappers import user, chat, updates
from .utils.json import dumps as dump_json

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
                name_mapping(trim_trailing_underscore=True),
                name_mapping(Update, map={"id": "update_id"}),
                name_mapping(Message, map={"id": "message_id"}),
                name_mapping(Result, map={"data": "result"}),
            ],
        )
        json_dumper = lambda value: dump_json(retort.dump(value))  # noqa

        if session_creator is None:
            from .impls.aiohttp_session import AiohttpSession

            session: Session = AiohttpSession(retort, token, api_url)
        else:
            session = session_creator(retort, token, api_url)

        self._session = session

        self.updates = updates.UpdatesApiWrapper(session, json_dumper)
        self.user = user.UserApiWrapper(session)
        self.chat = chat.ChatApiWrapper(json_dumper, session)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, _, exc, __):
        await self._session.finalize()

        if exc is not None:
            raise exc from exc

    @property
    def raw_session(self) -> Session:
        return self._session


__all__ = ["Bot"]
