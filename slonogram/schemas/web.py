from typing import Optional
from dataclasses import dataclass


@dataclass
class LoginUrl:
    url: str
    forward_text: Optional[str] = None
    bot_username: Optional[str] = None
    request_write_access: Optional[bool] = None


@dataclass
class WebAppInfo:
    url: str


@dataclass
class WebAppData:
    data: str
    button_text: str
