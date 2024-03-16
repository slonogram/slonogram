from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class WebAppInfo:
    url: str
    """ An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps """

    def alter(self, url: Omittable[Alterer1[str]] = OMIT):
        return WebAppInfo(
            url=alter1(url, self.url),
        )


__all__ = ["WebAppInfo"]
