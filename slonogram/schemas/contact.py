from __future__ import annotations
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class Contact:
    """This object represents a phone contact.

    Telegram documentation: https://core.telegram.org/bots/api#contact"""

    first_name: str
    """ Contact's first name """
    phone_number: str
    """ Contact's phone number """
    last_name: str | None = None
    """ Optional. Contact's last name """
    user_id: int | None = None
    """ Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. """
    vcard: str | None = None
    """ Optional. Additional data about the contact in the form of a vCard """

    def alter(
        self,
        first_name: Omittable[Alterer1[str]] = OMIT,
        phone_number: Omittable[Alterer1[str]] = OMIT,
        last_name: Omittable[Alterer1[str | None]] = OMIT,
        user_id: Omittable[Alterer1[int | None]] = OMIT,
        vcard: Omittable[Alterer1[str | None]] = OMIT,
    ) -> Contact:
        return Contact(
            first_name=alter1(first_name, self.first_name),
            phone_number=alter1(phone_number, self.phone_number),
            last_name=alter1(last_name, self.last_name),
            user_id=alter1(user_id, self.user_id),
            vcard=alter1(vcard, self.vcard),
        )


__all__ = ["Contact"]
