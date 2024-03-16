from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Location:
    """This object represents a point on the map.
    Telegram docs: https://core.telegram.org/bots/api#location"""

    heading: int
    """ Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only. """
    horizontal_accuracy: float
    """ Optional. The radius of uncertainty for the location, measured in meters; 0-1500 """
    latitude: float
    """ Latitude as defined by sender """
    live_period: int
    """ Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only. """
    longitude: float
    """ Longitude as defined by sender """
    proximity_alert_radius: int
    """ Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only. """

    def alter(
        self,
        latitude: Omittable[Alterer1[float]] = OMIT,
        longitude: Omittable[Alterer1[float]] = OMIT,
        heading: Omittable[Alterer1[int]] = OMIT,
        horizontal_accuracy: Omittable[Alterer1[float]] = OMIT,
        live_period: Omittable[Alterer1[int]] = OMIT,
        proximity_alert_radius: Omittable[Alterer1[int]] = OMIT,
    ) -> Location:
        return Location(
            latitude=alter1(latitude, self.latitude),
            longitude=alter1(longitude, self.longitude),
            heading=alter1(heading, self.heading),
            horizontal_accuracy=alter1(horizontal_accuracy, self.horizontal_accuracy),
            live_period=alter1(live_period, self.live_period),
            proximity_alert_radius=alter1(
                proximity_alert_radius, self.proximity_alert_radius
            ),
        )


__all__ = ["Location"]
