from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1
from slonogram.schemas import web_app_info as _web_app_info
from typing import TypeAlias


@model
class MenuButtonCommands:
    """Represents a menu button, which opens the bot's list of commands.
    Telegram docs: https://core.telegram.org/bots/api#menubuttoncommands"""

    type: str
    """ Type of the button, must be commands """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT) -> MenuButtonCommands:
        return MenuButtonCommands(
            type=alter1(type, self.type),
        )


@model
class MenuButtonDefault:
    """Describes that no specific value for the menu button was set.
    Telegram docs: https://core.telegram.org/bots/api#menubuttondefault"""

    type: str
    """ Type of the button, must be default """

    def alter(self, type: Omittable[Alterer1[str]] = OMIT) -> MenuButtonDefault:
        return MenuButtonDefault(
            type=alter1(type, self.type),
        )


@model
class MenuButtonWebApp:
    """Represents a menu button, which launches a Web App.
    Telegram docs: https://core.telegram.org/bots/api#menubuttonwebapp"""

    text: str
    """ Text on the button """
    type: str
    """ Type of the button, must be web_app """
    web_app: _web_app_info.WebAppInfo
    """ Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. """

    def alter(
        self,
        text: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        web_app: Omittable[Alterer1[_web_app_info.WebAppInfo]] = OMIT,
    ) -> MenuButtonWebApp:
        return MenuButtonWebApp(
            text=alter1(text, self.text),
            type=alter1(type, self.type),
            web_app=alter1(web_app, self.web_app),
        )


MenuButton: TypeAlias = MenuButtonCommands | MenuButtonWebApp | MenuButtonDefault
__all__ = ["MenuButtonCommands", "MenuButtonDefault", "MenuButtonWebApp", "MenuButton"]
