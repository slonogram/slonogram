# flake8: noqa
from typing import Awaitable, Optional, List, IO
from slonogram import schemas
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps


class UpdateCallGroup:
    __slots__ = ("_session",)

    def __init__(self, session: ApiSession) -> None:
        self._session = session

    def poll(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
    ) -> Awaitable[List[schemas.Update]]:
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
            params["allowed_updates"] = dumps(
                self._session.retort.dump(allowed_updates)
            )

        return self._session.call_method(
            List[schemas.Update], "getUpdates", params
        )

    def get_webhook_info(self) -> Awaitable[schemas.WebhookInfo]:
        """
        Use this method to get current webhook status. Requires no
        parameters. On success, returns a WebhookInfo object. If the bot
        is using getUpdates, will return an object with the url field
        empty. for more:
        https://core.telegram.org/bots/api#getwebhookinfo
        :return: See link mentioned above for more information
        """
        params: dict = {}

        return self._session.call_method(
            schemas.WebhookInfo, "getWebhookInfo", params
        )

    def delete_webhook(
        self, drop_pending_updates: Optional[bool] = None
    ) -> Awaitable[bool]:
        """
        Use this method to remove webhook integration if you decide to
        switch back to getUpdates. Returns True on success. for more:
        https://core.telegram.org/bots/api#deletewebhook
        :param drop_pending_updates: Pass True to drop all pending
                                     updates
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if drop_pending_updates is not None:
            params["drop_pending_updates"] = drop_pending_updates

        return self._session.call_method(bool, "deleteWebhook", params)

    def set_webhook(
        self,
        url: str,
        certificate: Optional[IO[bytes]] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        drop_pending_updates: Optional[bool] = None,
        secret_token: Optional[str] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to specify a URL and receive incoming updates via
        an outgoing webhook. Whenever there is an update for the bot, we
        will send an HTTPS POST request to the specified URL, containing
        a JSON-serialized Update. In case of an unsuccessful request, we
        will give up after a reasonable amount of attempts. Returns True
        on success. If you'd like to make sure that the webhook was set
        by you, you can specify secret data in the parameter
        secret_token. If specified, the request will contain a header
        "X-Telegram-Bot-Api-Secret-Token" with the secret token as
        content. for more: https://core.telegram.org/bots/api#setwebhook
        :param url: HTTPS URL to send updates to. Use an empty
                    string to remove webhook integration
        :param certificate: Upload your public key certificate so
                            that the root certificate in use can be
                            checked. See our self-signed guide for
                            details.
        :param ip_address: The fixed IP address which will be used
                           to send webhook requests instead of the
                           IP address resolved through DNS
        :param max_connections: The maximum allowed number of
                                simultaneous HTTPS connections to
                                the webhook for update delivery,
                                1-100. Defaults to 40. Use lower
                                values to limit the load on your
                                bot's server, and higher values to
                                increase your bot's throughput.
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
                                setWebhook, so unwanted updates may
                                be received for a short period of
                                time.
        :param drop_pending_updates: Pass True to drop all pending
                                     updates
        :param secret_token: A secret token to be sent in a header
                             "X-Telegram-Bot-Api-Secret-Token" in
                             every webhook request, 1-256
                             characters. Only characters A-Z, a-z,
                             0-9, _ and - are allowed. The header is
                             useful to ensure that the request comes
                             from a webhook set by you.
        :return: See link mentioned above for more information
        """
        params: dict = {"url": url}
        if certificate is not None:
            params["certificate"] = certificate

        if ip_address is not None:
            params["ip_address"] = ip_address

        if max_connections is not None:
            params["max_connections"] = max_connections

        if allowed_updates is not None:
            params["allowed_updates"] = allowed_updates

        if drop_pending_updates is not None:
            params["drop_pending_updates"] = drop_pending_updates

        if secret_token is not None:
            params["secret_token"] = secret_token

        return self._session.call_method(bool, "setWebhook", params)
