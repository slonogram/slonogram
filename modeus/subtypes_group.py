from .spec import Type

def _set(
    to: dict[str, dict[str, Type]],
    key1: str,
    key2: str,
    value: Type,
) -> None:
    if key1 in to:
        to[key1][key2] = value
    else:
        to[key1] = {key2: value}

def group_by_subtype(input: dict[str, Type]) -> dict[str, dict[str, Type]]:
    groups: dict[str, dict[str, Type]] = {}

    for type_name, desc in input.items():
        if desc.subtype_of:
            if len(desc.subtype_of) != 1:
                raise NotImplementedError(f"Number of parent types != 0 ({type_name!r})")

            parent = desc.subtype_of[0]
            _set(groups, parent, type_name, desc)
        elif not desc.subtypes:
            groups[type_name] = {type_name: desc}
        elif desc.subtypes:
            _set(groups, type_name, type_name, desc)

    return groups


__all__ = ["group_by_subtype"]

