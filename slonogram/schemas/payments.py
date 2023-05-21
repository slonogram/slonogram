from typing import Optional
from dataclasses import dataclass


@dataclass
class ShippingAddress:
    country_code: str
    state: str
    city: str

    street_line1: str
    street_line2: str

    post_code: str


@dataclass
class OrderInfo:
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    shipping_address: Optional[ShippingAddress] = None


@dataclass
class SuccessfulPayment:
    currency: str
    total_amount: int
    invoice_payload: str

    telegram_payment_charge_id: str
    provider_payment_charge_id: str

    shipping_option_id: Optional[int] = None
    order_info: Optional[OrderInfo] = None


@dataclass
class Invoice:
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int
