from slonogram.schemas.updates import Update


class BaseContext:
    def __init__(self, update: Update) -> None:
        self._update = update

    @property
    def update(self) -> Update:
        return self._update
