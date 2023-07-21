# flake8: noqa
from typing import Awaitable, Optional, List, IO
from slonogram import schemas
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps


class UserCallGroup:
    __slots__ = ("_session",)

    def __init__(self, session: ApiSession) -> None:
        self._session = session

    def get_me(self) -> Awaitable[schemas.User]:
        """
        A simple method for testing your bot's authentication token.
        Requires no parameters. Returns basic information about the bot
        in form of a User object. for more:
        https://core.telegram.org/bots/api#getme
        :return: See link mentioned above for more information
        """
        params: dict = {}

        return self._session.call_method(schemas.User, "getMe", params)

    def get_profile_photos(
        self,
        user_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Awaitable[schemas.UserProfilePhotos]:
        """
        Use this method to get a list of profile pictures for a user.
        Returns a UserProfilePhotos object. for more:
        https://core.telegram.org/bots/api#getuserprofilephotos
        :param user_id: Unique identifier of the target user
        :param offset: Sequential number of the first photo to be
                       returned. By default, all photos are
                       returned.
        :param limit: Limits the number of photos to be retrieved.
                      Values between 1-100 are accepted. Defaults to
                      100.
        :return: See link mentioned above for more information
        """
        params: dict = {"user_id": user_id}
        if offset is not None:
            params["offset"] = offset

        if limit is not None:
            params["limit"] = limit

        return self._session.call_method(
            schemas.UserProfilePhotos, "getUserProfilePhotos", params
        )

    def set_my_commands(
        self,
        commands: List[schemas.BotCommand],
        scope: Optional[schemas.BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to change the list of the bot's commands. See
        this manual for more details about bot commands. Returns True on
        success. for more:
        https://core.telegram.org/bots/api#setmycommands
        :param commands: A JSON-serialized list of bot commands to
                         be set as the list of the bot's commands.
                         At most 100 commands can be specified.
        :param scope: A JSON-serialized object, describing scope of
                      users for which the commands are relevant.
                      Defaults to BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, commands will be applied to
                              all users from the given scope, for
                              whose language there are no dedicated
                              commands
        :return: See link mentioned above for more information
        """
        params: dict = {"commands": commands}
        if scope is not None:
            params["scope"] = scope

        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(bool, "setMyCommands", params)

    def delete_my_commands(
        self,
        scope: Optional[schemas.BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to delete the list of the bot's commands for the
        given scope and user language. After deletion, higher level
        commands will be shown to affected users. Returns True on
        success. for more:
        https://core.telegram.org/bots/api#deletemycommands
        :param scope: A JSON-serialized object, describing scope of
                      users for which the commands are relevant.
                      Defaults to BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, commands will be applied to
                              all users from the given scope, for
                              whose language there are no dedicated
                              commands
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if scope is not None:
            params["scope"] = scope

        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(bool, "deleteMyCommands", params)

    def get_my_commands(
        self,
        scope: Optional[schemas.BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> Awaitable[List[schemas.BotCommand]]:
        """
        Use this method to get the current list of the bot's commands for
        the given scope and user language. Returns an Array of BotCommand
        objects. If commands aren't set, an empty list is returned. for
        more: https://core.telegram.org/bots/api#getmycommands
        :param scope: A JSON-serialized object, describing scope of
                      users. Defaults to BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code
                              or an empty string
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if scope is not None:
            params["scope"] = scope

        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(
            List[schemas.BotCommand], "getMyCommands", params
        )

    def set_my_name(
        self,
        name: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to change the bot's name. Returns True on
        success. for more: https://core.telegram.org/bots/api#setmyname
        :param name: New bot name; 0-64 characters. Pass an empty
                     string to remove the dedicated name for the
                     given language.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, the name will be shown to
                              all users for whose language there is
                              no dedicated name.
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if name is not None:
            params["name"] = name

        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(bool, "setMyName", params)

    def get_my_name(
        self, language_code: Optional[str] = None
    ) -> Awaitable[schemas.BotName]:
        """
        Use this method to get the current bot name for the given user
        language. Returns BotName on success. for more:
        https://core.telegram.org/bots/api#getmyname
        :param language_code: A two-letter ISO 639-1 language code
                              or an empty string
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(
            schemas.BotName, "getMyName", params
        )

    def set_my_description(
        self,
        description: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to change the bot's description, which is shown
        in the chat with the bot if the chat is empty. Returns True on
        success. for more:
        https://core.telegram.org/bots/api#setmydescription
        :param description: New bot description; 0-512 characters.
                            Pass an empty string to remove the
                            dedicated description for the given
                            language.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, the description will be
                              applied to all users for whose
                              language there is no dedicated
                              description.
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if description is not None:
            params["description"] = description

        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(bool, "setMyDescription", params)

    def get_my_description(
        self, language_code: Optional[str] = None
    ) -> Awaitable[schemas.BotDescription]:
        """
        Use this method to get the current bot description for the given
        user language. Returns BotDescription on success. for more:
        https://core.telegram.org/bots/api#getmydescription
        :param language_code: A two-letter ISO 639-1 language code
                              or an empty string
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(
            schemas.BotDescription, "getMyDescription", params
        )

    def set_my_short_description(
        self,
        short_description: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to change the bot's short description, which is
        shown on the bot's profile page and is sent together with the
        link when users share the bot. Returns True on success. for more:
        https://core.telegram.org/bots/api#setmyshortdescription
        :param short_description: New short description for the bot;
                                  0-120 characters. Pass an empty
                                  string to remove the dedicated
                                  short description for the given
                                  language.
        :param language_code: A two-letter ISO 639-1 language code.
                              If empty, the short description will
                              be applied to all users for whose
                              language there is no dedicated short
                              description.
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if short_description is not None:
            params["short_description"] = short_description

        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(
            bool, "setMyShortDescription", params
        )

    def get_my_short_description(
        self, language_code: Optional[str] = None
    ) -> Awaitable[schemas.BotShortDescription]:
        """
        Use this method to get the current bot short description for the
        given user language. Returns BotShortDescription on success. for
        more: https://core.telegram.org/bots/api#getmyshortdescription
        :param language_code: A two-letter ISO 639-1 language code
                              or an empty string
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if language_code is not None:
            params["language_code"] = language_code

        return self._session.call_method(
            schemas.BotShortDescription, "getMyShortDescription", params
        )

    def set_my_default_administrator_rights(
        self,
        rights: Optional[schemas.ChatAdministratorRights] = None,
        for_channels: Optional[bool] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to change the default administrator rights
        requested by the bot when it's added as an administrator to
        groups or channels. These rights will be suggested to users, but
        they are free to modify the list before adding the bot. Returns
        True on success. for more: https://core.telegram.org/bots/api#set
        mydefaultadministratorrights
        :param rights: A JSON-serialized object describing new
                       default administrator rights. If not
                       specified, the default administrator rights
                       will be cleared.
        :param for_channels: Pass True to change the default
                             administrator rights of the bot in
                             channels. Otherwise, the default
                             administrator rights of the bot for
                             groups and supergroups will be changed.
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if rights is not None:
            params["rights"] = rights

        if for_channels is not None:
            params["for_channels"] = for_channels

        return self._session.call_method(
            bool, "setMyDefaultAdministratorRights", params
        )

    def get_my_default_administrator_rights(
        self, for_channels: Optional[bool] = None
    ) -> Awaitable[schemas.ChatAdministratorRights]:
        """
        Use this method to get the current default administrator rights
        of the bot. Returns ChatAdministratorRights on success. for more:
        https://core.telegram.org/bots/api#getmydefaultadministratorright
        s
        :param for_channels: Pass True to get default administrator
                             rights of the bot in channels.
                             Otherwise, default administrator rights
                             of the bot for groups and supergroups
                             will be returned.
        :return: See link mentioned above for more information
        """
        params: dict = {}
        if for_channels is not None:
            params["for_channels"] = for_channels

        return self._session.call_method(
            schemas.ChatAdministratorRights,
            "getMyDefaultAdministratorRights",
            params,
        )
