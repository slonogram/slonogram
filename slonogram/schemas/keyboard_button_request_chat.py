from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import chat_administrator_rights as _chat_administrator_rights
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class KeyboardButtonRequestChat:
    """This object defines the criteria used to request a suitable chat. The identifier of the selected chat will be shared with the bot when the corresponding button is pressed. More about requesting chats: https://core.telegram.org/bots/features#chat-and-user-selection
    Telegram docs: https://core.telegram.org/bots/api#keyboardbuttonrequestchat"""

    bot_administrator_rights: _chat_administrator_rights.ChatAdministratorRights
    """ Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied. """
    bot_is_member: bool
    """ Optional. Pass True to request a chat with the bot as a member. Otherwise, no additional restrictions are applied. """
    chat_has_username: bool
    """ Optional. Pass True to request a supergroup or a channel with a username, pass False to request a chat without a username. If not specified, no additional restrictions are applied. """
    chat_is_channel: bool
    """ Pass True to request a channel chat, pass False to request a group or a supergroup chat. """
    chat_is_created: bool
    """ Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied. """
    chat_is_forum: bool
    """ Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat. If not specified, no additional restrictions are applied. """
    request_id: int
    """ Signed 32-bit identifier of the request, which will be received back in the ChatShared object. Must be unique within the message """
    user_administrator_rights: _chat_administrator_rights.ChatAdministratorRights
    """ Optional. A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied. """

    def alter(
        self,
        chat_is_channel: Omittable[Alterer1[bool]] = OMIT,
        request_id: Omittable[Alterer1[int]] = OMIT,
        bot_administrator_rights: Omittable[
            Alterer1[_chat_administrator_rights.ChatAdministratorRights]
        ] = OMIT,
        bot_is_member: Omittable[Alterer1[bool]] = OMIT,
        chat_has_username: Omittable[Alterer1[bool]] = OMIT,
        chat_is_created: Omittable[Alterer1[bool]] = OMIT,
        chat_is_forum: Omittable[Alterer1[bool]] = OMIT,
        user_administrator_rights: Omittable[
            Alterer1[_chat_administrator_rights.ChatAdministratorRights]
        ] = OMIT,
    ) -> KeyboardButtonRequestChat:
        return KeyboardButtonRequestChat(
            chat_is_channel=alter1(chat_is_channel, self.chat_is_channel),
            request_id=alter1(request_id, self.request_id),
            bot_administrator_rights=alter1(
                bot_administrator_rights, self.bot_administrator_rights
            ),
            bot_is_member=alter1(bot_is_member, self.bot_is_member),
            chat_has_username=alter1(chat_has_username, self.chat_has_username),
            chat_is_created=alter1(chat_is_created, self.chat_is_created),
            chat_is_forum=alter1(chat_is_forum, self.chat_is_forum),
            user_administrator_rights=alter1(
                user_administrator_rights, self.user_administrator_rights
            ),
        )


__all__ = ["KeyboardButtonRequestChat"]
