from __future__ import annotations
from slonogram.schemas import location as _location
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class Venue:
    """This object represents a venue.

    Telegram documentation: https://core.telegram.org/bots/api#venue"""

    address: str
    """ Address of the venue """
    location: _location.Location
    """ Venue location. Can't be a live location """
    title: str
    """ Name of the venue """
    foursquare_id: str | None = None
    """ Optional. Foursquare identifier of the venue """
    foursquare_type: str | None = None
    """ Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str | None = None
    """ Optional. Google Places identifier of the venue """
    google_place_type: str | None = None
    """ Optional. Google Places type of the venue. (See supported types.) """

    def alter(
        self,
        address: Omittable[Alterer1[str]] = OMIT,
        location: Omittable[Alterer1[_location.Location]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        foursquare_id: Omittable[Alterer1[str | None]] = OMIT,
        foursquare_type: Omittable[Alterer1[str | None]] = OMIT,
        google_place_id: Omittable[Alterer1[str | None]] = OMIT,
        google_place_type: Omittable[Alterer1[str | None]] = OMIT,
    ) -> Venue:
        return Venue(
            address=alter1(address, self.address),
            location=alter1(location, self.location),
            title=alter1(title, self.title),
            foursquare_id=alter1(foursquare_id, self.foursquare_id),
            foursquare_type=alter1(foursquare_type, self.foursquare_type),
            google_place_id=alter1(google_place_id, self.google_place_id),
            google_place_type=alter1(google_place_type, self.google_place_type),
        )


__all__ = ["Venue"]
