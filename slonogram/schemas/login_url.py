from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class LoginUrl:
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7.
    Telegram docs: https://core.telegram.org/bots/api#loginurl"""

    bot_username: str
    """ Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details. """
    forward_text: str
    """ Optional. New text of the button in forwarded messages. """
    request_write_access: bool
    """ Optional. Pass True to request the permission for your bot to send messages to the user. """
    url: str
    """ An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data. NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization. """

    def alter(
        self,
        url: Omittable[Alterer1[str]] = OMIT,
        bot_username: Omittable[Alterer1[str]] = OMIT,
        forward_text: Omittable[Alterer1[str]] = OMIT,
        request_write_access: Omittable[Alterer1[bool]] = OMIT,
    ) -> LoginUrl:
        return LoginUrl(
            url=alter1(url, self.url),
            bot_username=alter1(bot_username, self.bot_username),
            forward_text=alter1(forward_text, self.forward_text),
            request_write_access=alter1(
                request_write_access, self.request_write_access
            ),
        )


__all__ = ["LoginUrl"]
