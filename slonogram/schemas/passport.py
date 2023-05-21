from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class PassportElementType(str, Enum):
    personal_details = "personal_details"
    passport = "passport"
    driver_license = "driver_license"
    identity_card = "identity_card"
    internal_passport = "internal_passport"
    address = "address"
    utility_bill = "utility_bill"
    bank_statement = "bank_statement"
    rental_agreement = "rental_agreement"
    passport_registration = "passport_registration"
    temporary_registration = "temporary_registration"
    phone_number = "phone_number"
    email = "email"


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
