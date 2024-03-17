from __future__ import annotations
from slonogram.schemas import (
    encrypted_credentials as _encrypted_credentials,
    encrypted_passport_element as _encrypted_passport_element,
)
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from slonogram._internal.utils import model


@model
class PassportData:
    """Describes Telegram Passport data shared with the bot by the user.

    Telegram documentation: https://core.telegram.org/bots/api#passportdata"""

    credentials: _encrypted_credentials.EncryptedCredentials
    """ Encrypted credentials required to decrypt the data """
    data: tuple[_encrypted_passport_element.EncryptedPassportElement, ...]
    """ Array with information about documents and other Telegram Passport elements that was shared with the bot """

    def alter(
        self,
        credentials: Omittable[
            Alterer1[_encrypted_credentials.EncryptedCredentials]
        ] = OMIT,
        data: Omittable[
            Alterer1[tuple[_encrypted_passport_element.EncryptedPassportElement, ...]]
        ] = OMIT,
    ) -> PassportData:
        return PassportData(
            credentials=alter1(credentials, self.credentials),
            data=alter1(data, self.data),
        )


__all__ = ["PassportData"]
