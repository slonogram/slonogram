from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class PassportElementType(str, Enum):
    PERSONAL_DETAILS = "personal_details"
    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"
    ADDRESS = "address"
    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    RENTAL_AGREEMENT = "rental_agreement"
    PASSPORT_REGISTRATION = "passport_registration"
    TEMPORARY_REGISTRATION = "temporary_registration"
    PHONE_NUMBER = "phone_number"
    EMAIL = "email"


@dataclass(slots=True)
class PassportData:
    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials


@dataclass(slots=True)
class PassportFile:
    file_id: str
    file_unique_id: str

    file_size: int
    file_date: int


@dataclass(slots=True)
class EncryptedCredentials:
    data: str
    hash: str
    secret: str


@dataclass(slots=True)
class EncryptedPassportElement:
    type_: PassportElementType
    hash: str

    data: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None

    files: Optional[List[PassportFile]] = None
    front_side: Optional[PassportFile] = None
    reverse_side: Optional[PassportFile] = None
    selfie: Optional[PassportFile] = None
    translation: Optional[PassportFile] = None


__all__ = [
    "EncryptedPassportElement",
    "EncryptedCredentials",
    "PassportFile",
    "PassportData",
    "PassportElementType",
]
