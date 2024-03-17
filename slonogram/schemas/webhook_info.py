from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class WebhookInfo:
    """Describes the current status of a webhook.

    Telegram documentation: https://core.telegram.org/bots/api#webhookinfo"""

    has_custom_certificate: bool
    """ True, if a custom certificate was provided for webhook certificate checks """
    pending_update_count: int
    """ Number of updates awaiting delivery """
    url: str
    """ Webhook URL, may be empty if webhook is not set up """
    allowed_updates: tuple[str, ...] | None = None
    """ Optional. A list of update types the bot is subscribed to. Defaults to all update types except chat_member """
    ip_address: str | None = None
    """ Optional. Currently used webhook IP address """
    last_error_date: int | None = None
    """ Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook """
    last_error_message: str | None = None
    """ Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook """
    last_synchronization_error_date: int | None = None
    """ Optional. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters """
    max_connections: int | None = None
    """ Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery """

    def alter(
        self,
        has_custom_certificate: Omittable[Alterer1[bool]] = OMIT,
        pending_update_count: Omittable[Alterer1[int]] = OMIT,
        url: Omittable[Alterer1[str]] = OMIT,
        allowed_updates: Omittable[Alterer1[tuple[str, ...] | None]] = OMIT,
        ip_address: Omittable[Alterer1[str | None]] = OMIT,
        last_error_date: Omittable[Alterer1[int | None]] = OMIT,
        last_error_message: Omittable[Alterer1[str | None]] = OMIT,
        last_synchronization_error_date: Omittable[Alterer1[int | None]] = OMIT,
        max_connections: Omittable[Alterer1[int | None]] = OMIT,
    ) -> WebhookInfo:
        return WebhookInfo(
            has_custom_certificate=alter1(
                has_custom_certificate, self.has_custom_certificate
            ),
            pending_update_count=alter1(
                pending_update_count, self.pending_update_count
            ),
            url=alter1(url, self.url),
            allowed_updates=alter1(allowed_updates, self.allowed_updates),
            ip_address=alter1(ip_address, self.ip_address),
            last_error_date=alter1(last_error_date, self.last_error_date),
            last_error_message=alter1(last_error_message, self.last_error_message),
            last_synchronization_error_date=alter1(
                last_synchronization_error_date, self.last_synchronization_error_date
            ),
            max_connections=alter1(max_connections, self.max_connections),
        )


__all__ = ["WebhookInfo"]
