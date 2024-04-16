from typing import TYPE_CHECKING

from .base import Session

if TYPE_CHECKING:
    from .middleware import SessionMiddleware


class ExtendedSession(Session):
    def after(self, *middlewares: 'SessionMiddleware') -> 'ExtendedSession':
        from .middleware import Follows

        return Follows.from_iterable(self, middlewares)

def extend_session(bare: Session) -> ExtendedSession:
    from .middleware import Follows

    return Follows(bare, lambda req, next: next(req))


__all__ = ["ExtendedSession", "extend_session"]

