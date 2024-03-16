from ..type_parser import Tracker, no_tracking

def create_type_alias(
    name: str,
    tp: str,
    tracker: Tracker = no_tracking,
) -> str:
    tracker('typing', 'TypeAlias')

    return (
        f"{name}: TypeAlias = {tp}"
    )

__all__ = ["create_type_alias"]
