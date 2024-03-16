from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class VideoChatParticipantsInvited:
    """This object represents a service message about new members invited to a video chat.
    Telegram docs: https://core.telegram.org/bots/api#videochatparticipantsinvited"""

    users: list[_user.User]
    """ New members that were invited to the video chat """

    def alter(
        self, users: Omittable[Alterer1[list[_user.User]]] = OMIT
    ) -> VideoChatParticipantsInvited:
        return VideoChatParticipantsInvited(
            users=alter1(users, self.users),
        )


__all__ = ["VideoChatParticipantsInvited"]
