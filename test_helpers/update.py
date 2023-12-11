from random import randint
from slonogram import schemas


def update(
    update_id: int | None = None,
    message: schemas.Message | None = None,
) -> schemas.Update:
    upd_id = update_id or randint(0, 2**32)
    return schemas.Update(update_id=upd_id, message=message)


__all__ = ["update"]
