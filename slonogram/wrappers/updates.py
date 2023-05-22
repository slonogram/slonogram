from typing import Optional, List, Any, Dict, BinaryIO
from adaptix.struct_path import ExcPathRenderer

from ..schemas.updates import Update, UpdateType
from ..schemas.webhook import WebhookInfo

from ..utils.dict import set_if_not_none, JsonDumper
from ..protocols.session import Session


class UpdatesApiWrapper:
    def __init__(self, session: Session, json_dumper: JsonDumper) -> None:
        self._session = session
        self._json_dumper = json_dumper

    async def get_webhook_info(self) -> WebhookInfo:
        return (
            await self._session.raw_method(
                WebhookInfo, "getWebhookInfo", {}
            )
        ).unwrap_data()

    async def set_webhook(
        self,
        url: str,
        certificate: Optional[str | BinaryIO] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[UpdateType]] = None,
        drop_pending_updates: Optional[bool] = None,
        secret_token: Optional[str] = None,
    ) -> Optional[str]:
        args: Dict[str, Any] = {"url": url}
        set_if_not_none(
            args,
            (
                ("certificate", certificate),
                ("ip_address", ip_address),
                ("max_connections", max_connections),
                ("drop_pending_updates", drop_pending_updates),
                ("secret_token", secret_token),
                ("allowed_updates", allowed_updates, self._json_dumper),
            ),
        )

        return (
            await self._session.raw_method(
                Any, "setWebhook", args  # type: ignore
            )
        ).description

    async def delete_webhook(self, drop_pending_updates: bool) -> bool:
        args = {"drop_pending_updates": drop_pending_updates}
        return (
            await self._session.raw_method(bool, "deleteWebhook", args)
        ).unwrap_data()

    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[UpdateType]] = None,
    ) -> List[Update]:
        args: Dict[str, Any] = {}
        set_if_not_none(
            args,
            (
                ("offset", offset),
                ("limit", limit),
                ("timeout", timeout),
                ("allowed_updates", allowed_updates, self._json_dumper),
            ),
        )

        with ExcPathRenderer():
            return (
                await self._session.raw_method(
                    List[Update], "getUpdates", args
                )
            ).unwrap_data()


__all__ = ["UpdatesApiWrapper"]
