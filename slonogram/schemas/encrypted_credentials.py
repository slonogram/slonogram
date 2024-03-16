from __future__ import annotations
from slonogram._internal.utils import model
from slonogram.omittable import OMIT, Omittable
from slonogram.altering import Alterer1, alter1


@model
class EncryptedCredentials:
    """Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.
    Telegram docs: https://core.telegram.org/bots/api#encryptedcredentials"""

    data: str
    """ Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication """
    hash: str
    """ Base64-encoded data hash for data authentication """
    secret: str
    """ Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption """

    def alter(
        self,
        data: Omittable[Alterer1[str]] = OMIT,
        hash: Omittable[Alterer1[str]] = OMIT,
        secret: Omittable[Alterer1[str]] = OMIT,
    ):
        return EncryptedCredentials(
            data=alter1(data, self.data),
            hash=alter1(hash, self.hash),
            secret=alter1(secret, self.secret),
        )


__all__ = ["EncryptedCredentials"]
