from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class WriteAccessAllowed:
    from_attachment_menu: bool
    """ Optional. True, if the access was granted when the bot was added to the attachment or side menu """
    from_request: bool
    """ Optional. True, if the access was granted after the user accepted an explicit request from a Web App sent by the method requestWriteAccess """
    web_app_name: str
    """ Optional. Name of the Web App, if the access was granted when the Web App was launched from a link """

    def alter(
        self,
        from_attachment_menu: Omittable[Alterer1[bool]] = OMIT,
        from_request: Omittable[Alterer1[bool]] = OMIT,
        web_app_name: Omittable[Alterer1[str]] = OMIT,
    ):
        return WriteAccessAllowed(
            from_attachment_menu=alter1(
                from_attachment_menu, self.from_attachment_menu
            ),
            from_request=alter1(from_request, self.from_request),
            web_app_name=alter1(web_app_name, self.web_app_name),
        )


__all__ = ["WriteAccessAllowed"]
