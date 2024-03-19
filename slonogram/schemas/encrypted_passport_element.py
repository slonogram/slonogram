"""@generated using `modeus`
BotAPI version: Bot API 7.1
BotAPI changelog: https://core.telegram.org/bots/api#february-16-2024
BotAPI release date: February 16, 2024
"""
from __future__ import annotations
from slonogram.schemas import passport_file as _passport_file
from slonogram.omittable import Omittable, OMIT
from slonogram.altering import Alterer1, alter1
from dataclasses import dataclass


@dataclass(slots=True)
class EncryptedPassportElement:
    """Describes documents or other Telegram Passport elements shared with
    the bot by the user.  Telegram documentation:
    https://core.telegram.org/bots/api#encryptedpassportelement"""

    hash: str
    """Base64-encoded element hash for using in
    PassportElementErrorUnspecified"""
    type: str
    """Element type. One of "personal_details", "passport", "driver_license",
    "identity_card", "internal_passport", "address", "utility_bill",
    "bank_statement", "rental_agreement", "passport_registration",
    "temporary_registration", "phone_number", "email"."""
    data: str | None = None
    """Optional. Base64-encoded encrypted Telegram Passport element data
    provided by the user; available only for "personal_details",
    "passport", "driver_license", "identity_card", "internal_passport" and
    "address" types. Can be decrypted and verified using the accompanying
    EncryptedCredentials."""
    email: str | None = None
    """Optional. User's verified email address; available only for "email"
    type"""
    files: tuple[_passport_file.PassportFile, ...] | None = None
    """Optional. Array of encrypted files with documents provided by the
    user; available only for "utility_bill", "bank_statement",
    "rental_agreement", "passport_registration" and
    "temporary_registration" types. Files can be decrypted and verified
    using the accompanying EncryptedCredentials."""
    front_side: _passport_file.PassportFile | None = None
    """Optional. Encrypted file with the front side of the document, provided
    by the user; available only for "passport", "driver_license",
    "identity_card" and "internal_passport". The file can be decrypted and
    verified using the accompanying EncryptedCredentials."""
    phone_number: str | None = None
    """Optional. User's verified phone number; available only for
    "phone_number" type"""
    reverse_side: _passport_file.PassportFile | None = None
    """Optional. Encrypted file with the reverse side of the document,
    provided by the user; available only for "driver_license" and
    "identity_card". The file can be decrypted and verified using the
    accompanying EncryptedCredentials."""
    selfie: _passport_file.PassportFile | None = None
    """Optional. Encrypted file with the selfie of the user holding a
    document, provided by the user; available if requested for "passport",
    "driver_license", "identity_card" and "internal_passport". The file
    can be decrypted and verified using the accompanying
    EncryptedCredentials."""
    translation: tuple[_passport_file.PassportFile, ...] | None = None
    """Optional. Array of encrypted files with translated versions of
    documents provided by the user; available if requested for "passport",
    "driver_license", "identity_card", "internal_passport",
    "utility_bill", "bank_statement", "rental_agreement",
    "passport_registration" and "temporary_registration" types. Files can
    be decrypted and verified using the accompanying EncryptedCredentials."""

    def alter(
        self,
        hash: Omittable[Alterer1[str]] = OMIT,
        type: Omittable[Alterer1[str]] = OMIT,
        data: Omittable[Alterer1[str | None]] = OMIT,
        email: Omittable[Alterer1[str | None]] = OMIT,
        files: Omittable[
            Alterer1[tuple[_passport_file.PassportFile, ...] | None]
        ] = OMIT,
        front_side: Omittable[Alterer1[_passport_file.PassportFile | None]] = OMIT,
        phone_number: Omittable[Alterer1[str | None]] = OMIT,
        reverse_side: Omittable[Alterer1[_passport_file.PassportFile | None]] = OMIT,
        selfie: Omittable[Alterer1[_passport_file.PassportFile | None]] = OMIT,
        translation: Omittable[
            Alterer1[tuple[_passport_file.PassportFile, ...] | None]
        ] = OMIT,
    ) -> EncryptedPassportElement:
        return EncryptedPassportElement(
            hash=alter1(hash, self.hash),
            type=alter1(type, self.type),
            data=alter1(data, self.data),
            email=alter1(email, self.email),
            files=alter1(files, self.files),
            front_side=alter1(front_side, self.front_side),
            phone_number=alter1(phone_number, self.phone_number),
            reverse_side=alter1(reverse_side, self.reverse_side),
            selfie=alter1(selfie, self.selfie),
            translation=alter1(translation, self.translation),
        )


__all__ = ["EncryptedPassportElement"]
