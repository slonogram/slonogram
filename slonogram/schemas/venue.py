from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import location as _location
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class Venue:
    address: str
    """ Address of the venue """
    foursquare_id: str
    """ Optional. Foursquare identifier of the venue """
    foursquare_type: str
    """ Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".) """
    google_place_id: str
    """ Optional. Google Places identifier of the venue """
    google_place_type: str
    """ Optional. Google Places type of the venue. (See supported types.) """
    location: _location.Location
    """ Venue location. Can't be a live location """
    title: str
    """ Name of the venue """

    def alter(
        self,
        address: Omittable[Alterer1[str]] = OMIT,
        location: Omittable[Alterer1[_location.Location]] = OMIT,
        title: Omittable[Alterer1[str]] = OMIT,
        foursquare_id: Omittable[Alterer1[str]] = OMIT,
        foursquare_type: Omittable[Alterer1[str]] = OMIT,
        google_place_id: Omittable[Alterer1[str]] = OMIT,
        google_place_type: Omittable[Alterer1[str]] = OMIT,
    ):
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
