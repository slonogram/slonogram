from ..typing.tracking import Tracker

def create_type_alias(
    name: str,
    tp: str,
    docs: str,
    tracker: Tracker,
) -> str:
    return (
        f"{name}: {tracker('typing', 'TypeAlias')} = {tp}"
        + '\n'
        + f'""" {docs} """'
    )

__all__ = ["create_type_alias"]
