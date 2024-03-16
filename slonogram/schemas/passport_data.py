from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.schemas import (
    encrypted_credentials as _encrypted_credentials,
    encrypted_passport_element as _encrypted_passport_element,
)
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class PassportData:
    credentials: _encrypted_credentials.EncryptedCredentials
    """ Encrypted credentials required to decrypt the data """
    data: list[_encrypted_passport_element.EncryptedPassportElement]
    """ Array with information about documents and other Telegram Passport elements that was shared with the bot """

    def alter(
        self,
        credentials: Omittable[
            Alterer1[_encrypted_credentials.EncryptedCredentials]
        ] = OMIT,
        data: Omittable[
            Alterer1[list[_encrypted_passport_element.EncryptedPassportElement]]
        ] = OMIT,
    ):
        return PassportData(
            credentials=alter1(credentials, self.credentials),
            data=alter1(data, self.data),
        )


__all__ = ["PassportData"]
