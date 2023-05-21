from typing import Optional
from dataclasses import dataclass


@dataclass(slots=True)
class LoginUrl:
    url: str
    forward_text: Optional[str] = None
    bot_username: Optional[str] = None
    request_write_access: Optional[bool] = None


@dataclass(slots=True)
class WebAppInfo:
    url: str


@dataclass(slots=True)
class WebAppData:
    data: str
    button_text: str


__all__ = ["LoginUrl", "WebAppInfo", "WebAppData"]
