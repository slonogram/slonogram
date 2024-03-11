from dataclasses import dataclass
from .spec import Type


@dataclass(slots=True, frozen=True)
class SubtypesGrouped:
    subtyped: dict[str, dict[str, Type]]
    free: dict[str, Type]


def group_by_subtype(types: dict[str, Type]) -> SubtypesGrouped:
    subtyped: dict[str, dict[str, Type]] = {}
    free: dict[str, Type] = {}
    parents: set[str] = set()

    for name, tp in types.items():
        if len(tp.subtype_of) > 1:
            raise NotImplementedError(f'Type {name!r} has more subtype_of than one: {tp!r}')
        elif tp.subtype_of:
            parent = tp.subtype_of[0]
            if parent not in subtyped:
                parents.add(parent)
                subtyped[parent] = {name: tp}
            else:
                subtyped[parent][name] = tp
        else:
            free[name] = tp

    return SubtypesGrouped(
        subtyped,
        {k:v for k, v in free.items() if k not in parents}
    )

__all__ = [
    "SubtypesGrouped",
    "group_by_subtype",
]
