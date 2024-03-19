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
class ProximityAlertTriggered:
    """This object represents the content of a service message, sent whenever
    a user in the chat triggers a proximity alert set by another user.
    Telegram documentation:
    https://core.telegram.org/bots/api#proximityalerttriggered"""

    distance: int
    """The distance between the users"""
    traveler: _user.User
    """User that triggered the alert"""
    watcher: _user.User
    """User that set the alert"""

    def alter(
        self,
        distance: Omittable[Alterer1[int]] = OMIT,
        traveler: Omittable[Alterer1[_user.User]] = OMIT,
        watcher: Omittable[Alterer1[_user.User]] = OMIT,
    ) -> ProximityAlertTriggered:
        return ProximityAlertTriggered(
            distance=alter1(distance, self.distance),
            traveler=alter1(traveler, self.traveler),
            watcher=alter1(watcher, self.watcher),
        )


__all__ = ["ProximityAlertTriggered"]
