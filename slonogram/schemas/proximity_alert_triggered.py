from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import user as _user
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ProximityAlertTriggered:
    distance: int
    """ The distance between the users """
    traveler: _user.User
    """ User that triggered the alert """
    watcher: _user.User
    """ User that set the alert """

    def alter(
        self,
        distance: Omittable[Alterer1[int]] = OMIT,
        traveler: Omittable[Alterer1[_user.User]] = OMIT,
        watcher: Omittable[Alterer1[_user.User]] = OMIT,
    ):
        return ProximityAlertTriggered(
            distance=alter1(distance, self.distance),
            traveler=alter1(traveler, self.traveler),
            watcher=alter1(watcher, self.watcher),
        )


__all__ = ["ProximityAlertTriggered"]
