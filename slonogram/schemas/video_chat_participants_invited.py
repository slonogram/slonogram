"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import user as _user
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class VideoChatParticipantsInvited:
    """This object represents a service message about new members invited to
    a video chat.  Telegram documentation:
    https://core.telegram.org/bots/api#videochatparticipantsinvited"""

    users: tuple[_user.User, ...]
    """New members that were invited to the video chat"""

    def alter(
        self, users: Omittable[Alterer1[tuple[_user.User, ...]]] = OMIT
    ) -> VideoChatParticipantsInvited:
        return VideoChatParticipantsInvited(
            users=alter1(users, self.users),
        )


__all__ = ["VideoChatParticipantsInvited"]
