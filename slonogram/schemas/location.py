from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class Location:
    """This object represents a point on the map.

    Telegram documentation: https://core.telegram.org/bots/api#location"""

    latitude: float
    """ Latitude as defined by sender """
    longitude: float
    """ Longitude as defined by sender """
    heading: int | None = None
    """ Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only. """
    horizontal_accuracy: float | None = None
    """ Optional. The radius of uncertainty for the location, measured in meters; 0-1500 """
    live_period: int | None = None
    """ Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only. """
    proximity_alert_radius: int | None = None
    """ Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only. """

    def alter(
        self,
        latitude: Omittable[Alterer1[float]] = OMIT,
        longitude: Omittable[Alterer1[float]] = OMIT,
        heading: Omittable[Alterer1[int | None]] = OMIT,
        horizontal_accuracy: Omittable[Alterer1[float | None]] = OMIT,
        live_period: Omittable[Alterer1[int | None]] = OMIT,
        proximity_alert_radius: Omittable[Alterer1[int | None]] = OMIT,
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
