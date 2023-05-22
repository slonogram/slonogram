from typing import Optional
from dataclasses import dataclass

from .updates import UpdateType


@dataclass(slots=True)
class WebhookInfo:
    url: str
    has_custom_certificate: bool
    pending_update_count: int

    ip_address: Optional[str] = None
    last_error_date: Optional[int] = None
    last_error_message: Optional[str] = None
    last_synchronization_error_date: Optional[int] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[UpdateType] = None


__all__ = ["WebhookInfo"]
