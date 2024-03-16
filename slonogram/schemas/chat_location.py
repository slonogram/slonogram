from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import location as _location
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class ChatLocation:
    address: str
    """ Location address; 1-64 characters, as defined by the chat owner """
    location: _location.Location
    """ The location to which the supergroup is connected. Can't be a live location. """

    def alter(
        self,
        address: Omittable[Alterer1[str]] = OMIT,
        location: Omittable[Alterer1[_location.Location]] = OMIT,
    ):
        return ChatLocation(
            address=alter1(address, self.address),
            location=alter1(location, self.location),
        )


__all__ = ["ChatLocation"]
