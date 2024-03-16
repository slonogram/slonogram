from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import web_app_info as _web_app_info
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class InlineQueryResultsButton:
    """This object represents a button to be shown above inline query results. You must use exactly one of the optional fields.
    Telegram docs: https://core.telegram.org/bots/api#inlinequeryresultsbutton"""

    start_parameter: str
    """ Optional. Deep-linking parameter for the /start message sent to the bot when a user presses the button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed. Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities. """
    text: str
    """ Label text on the button """
    web_app: _web_app_info.WebAppInfo
    """ Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to switch back to the inline mode using the method switchInlineQuery inside the Web App. """

    def alter(
        self,
        text: Omittable[Alterer1[str]] = OMIT,
        start_parameter: Omittable[Alterer1[str]] = OMIT,
        web_app: Omittable[Alterer1[_web_app_info.WebAppInfo]] = OMIT,
    ) -> InlineQueryResultsButton:
        return InlineQueryResultsButton(
            text=alter1(text, self.text),
            start_parameter=alter1(start_parameter, self.start_parameter),
            web_app=alter1(web_app, self.web_app),
        )


__all__ = ["InlineQueryResultsButton"]
