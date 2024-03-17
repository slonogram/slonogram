from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class WebAppInfo:
    """Describes a Web App.

    Telegram documentation: https://core.telegram.org/bots/api#webappinfo"""

    url: str
    """ An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps """

    def alter(self, url: Omittable[Alterer1[str]] = OMIT) -> WebAppInfo:
        return WebAppInfo(
            url=alter1(url, self.url),
        )


__all__ = ["WebAppInfo"]
