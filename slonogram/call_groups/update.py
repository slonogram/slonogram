from typing import Awaitable, Optional, List  # noqa
import slonogram.schemas  # noqa
from adaptix import Retort
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps  # noqa


class UpdateCallGroup:
    __slots__ = "_retort", "_session"

    def __init__(self, session: ApiSession, retort: Retort) -> None:
        self._session = session
        self._retort = retort

    async def poll(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
    ) -> List[slonogram.schemas.Update]:
        """
        Use this method to receive incoming updates using long polling
        (wiki). Returns an Array of Update objects. for more:
        https://core.telegram.org/bots/api#getupdates
        :param offset: Identifier of the first update to be
                       returned. Must be greater by one than the
                       highest among the identifiers of previously
                       received updates. By default, updates
                       starting with the earliest unconfirmed update
                       are returned. An update is considered
                       confirmed as soon as getUpdates is called
                       with an offset higher than its update_id. The
                       negative offset can be specified to retrieve
                       updates starting from -offset update from the
                       end of the updates queue. All previous
                       updates will be forgotten.
        :param limit: Limits the number of updates to be retrieved.
                      Values between 1-100 are accepted. Defaults to
                      100.
        :param timeout: Timeout in seconds for long polling.
                        Defaults to 0, i.e. usual short polling.
                        Should be positive, short polling should be
                        used for testing purposes only.
        :param allowed_updates: A JSON-serialized list of the update
                                types you want your bot to receive.
                                For example, specify ["message",
                                "edited_channel_post",
                                "callback_query"] to only receive
                                updates of these types. See Update
                                for a complete list of available
                                update types. Specify an empty list
                                to receive all update types except
                                chat_member (default). If not
                                specified, the previous setting will
                                be used. Please note that this
                                parameter doesn't affect updates
                                created before the call to the
                                getUpdates, so unwanted updates may
                                be received for a short period of
                                time.
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if offset is not None:
            params["offset"] = offset

        if limit is not None:
            params["limit"] = limit

        if timeout is not None:
            params["timeout"] = timeout

        if allowed_updates is not None:
            params["allowed_updates"] = allowed_updates

        return self._retort.load(
            await self._session.call_method("getUpdates", params),
            List[slonogram.schemas.Update],
        )
