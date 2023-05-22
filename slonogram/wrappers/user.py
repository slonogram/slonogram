from ..schemas.user import User
from ..protocols.session import Session


class UserApiWrapper:
    def __init__(self, session: Session) -> None:
        self._session = session

    async def me(self) -> User:
        return (
            await self._session.raw_method(User, "getMe", {})
        ).unwrap_data()


__all__ = ["UserApiWrapper"]
